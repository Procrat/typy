import re, urllib.request, urllib.parse, urllib.error, time, sys, pickle

# Part 1 : web crawling
# argument: the starting link to crawl from
# return values: array of crawled links, dict of parent -> children links, dict of anchor text -> links, dict of terms per page
def crawl(start_link):
    crawled = []
    children = dict()
    anchors = dict()
    text_content = dict()

    def crawl_recursive(link):
        # leave the server alone for a short time
        time.sleep(0.05);

        crawled.append(link)
        content = urllib.request.urlopen(link).read()
        # get all words on the page
        text_content[link] = (re.sub(r"<[^>]*>", "", content)).lower().split()

        # get all links on the page
        for i in re.findall('<a.*>.*</a>', content, re.IGNORECASE):
            base = re.sub('/[^/]*$','/', link)
            anch = (re.search(r"<a.*>(.*)</a>", i)).group(1)
            l = (re.search(r"href=\"(.*)\"", i)).group(1)

            # add anchor text per link
            if base+l in anchors:
                anchors[base+l].append(anch.lower())
            else:
                anchors[base+l] = [anch.lower()]

            # add parent-child link
            if link in children:
                children[link].append(base+l)
            else:
                children[link] = [base+l]

            # entering a loop, go to next link
            if base+l in crawled:
                continue

            crawl_recursive(base+l)


    crawl_recursive(start_link)
    return(crawled, children, anchors, text_content)


# Part 2: PageRank
# arguments: dict of parent->children links, array of all links
# return value: the pagerank vector; the indices are the same indices as in the array of all links
def pagerank(children, crawled):

    pr = dict()
    n = len(crawled)
    pi = [0] * n
    pi[0] = 1
    alpha = 0.1
    diff = [1] * n

    # put all non-zero values of the transition matrix in a dictionary
    for link in crawled:
        if link in children:
            for i in range(len(children[link])):
                # if the same page links to the same child twice, there's a higher chance to go to that child
                if (crawled.index(link),crawled.index(children[link][i])) not in pr:
                    pr[crawled.index(link),crawled.index(children[link][i])] = 1/float(len(children[link]))
                else:
                    pr[crawled.index(link),crawled.index(children[link][i])] += 1/float(len(children[link]))


    while sum(diff) > 0.01:
        solution = [0] * n

        # loop over matrix column per column
        for j in range(n):
            for i in range(n):

                # get the value in place (i, j): either a value as calculated above, or a teleportation value
                if crawled[i] not in children:
                    value = 1 / float(n)
                else:
                    if (i,j) in pr:
                        value = pr[i,j]*(1-alpha)
                    else:
                        value = alpha/(n - len(children[crawled[i]]))

                solution[j] += pi[i]*value

        # calculate the difference between the last pagerank vector and the current solution to check if we can stop
        for k in range(len(pi)):
            diff[k] = abs(pi[k]-solution[k])

        pi = solution

    return pi



# Part 3: Search
# arguments: array of search terms, dict of anchor->links, dict of terms per page, pagerank array, array of all links
# return value: array of max. 10 links in order of their pagerank
def search(terms, anchors, text_content, pr, crawled):
    found = []
    index_array = dict()

    terms = [x.lower() for x in terms]
    for term in terms:
        index_array[term] = []
        for i in range(len(crawled)):
            # search for term in text on page
            if term in text_content[crawled[i]]:
                if i not in index_array[term]:
                    index_array[term].append(i)

            # search for term in anchor text linking to page
            if crawled[i] in anchors:
                for anch in anchors[crawled[i]]:
                    if term in anch.split():
                        if i not in index_array[term]:
                            index_array[term].append(i)

    indices = index_array[terms[0]]

    # find intersection of all terms
    for i in range(1,len(index_array)):
        temp = [x for x in indices if x in index_array[terms[i]]]
        indices = temp

    # sort indices in order of their pagerank
    indices.sort(key=lambda x: pr[x], reverse=True)

    # get a maximum of ten indices
    indices = indices[:10]

    # get links corresponding these indices
    found = [crawled[l] for l in indices]
    return found




if sys.argv[1] == "make":
    crawled, children, anchors, text_content = crawl(sys.argv[2])
    pr = pagerank(children, crawled)
    mean_links = len(sum(list(children.values()),[]))/float(len(crawled))

    print("Number of documents crawled: " + str(len(crawled)))

    # I wasn't sure if the distinct terms referred to anchor text or all text, so I printed both
    print("Number of distinct anchor terms: " + str(len(set(sum(list(anchors.values()),[])))))
    print("Number of distinct terms (all): " + str(len(set(sum(list(text_content.values()),[])))))

    # This is always the same: an outgoing link on a page is an incoming link for another page
    print("Mean number of incoming links: " + str(mean_links))
    print("Mean number of links per page: " + str(mean_links))
	
    # Put all relevant data for querying in file data.pkl
    output = open('data.pkl', 'wb')
    pickle.dump([anchors, text_content, pr, crawled], output)


if sys.argv[1] == "query":
    data = open('data.pkl', 'rb')
    anchors, text_content, pr, crawled = pickle.load(data)

    # get terms from command line
    terms = sys.argv[2:]
    found = search(terms, anchors, text_content, pr, crawled)
    for i in found:
        print(i)
