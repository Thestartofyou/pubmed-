from Bio import Entrez

# set email to identify yourself to PubMed API
Entrez.email = "your.email@example.com"

# search query for clinical trials with pending status
search_query = "(clinical trial[Publication Type] OR clinical trials as topic[MeSH Terms]) AND pending[Status]"

# use the PubMed API to search for the query and get the search results
handle = Entrez.esearch(db="pubmed", term=search_query, retmax=10)
search_results = Entrez.read(handle)

# retrieve the PubMed IDs for the search results
id_list = search_results["IdList"]

# use the PubMed API to retrieve the details for each clinical trial
for pubmed_id in id_list:
    handle = Entrez.esummary(db="pubmed", id=pubmed_id)
    summary_results = Entrez.read(handle)

    # extract the relevant information from the summary results
    title = summary_results[0]["Title"]
    status = summary_results[0]["PubStatus"]
    url = "https://pubmed.ncbi.nlm.nih.gov/" + pubmed_id

    # print the information for the clinical trial
    print(f"Title: {title}\nStatus: {status}\nURL: {url}\n")
