from entrezpy.esearch.esearcher import Esearcher
from entrezpy.efetch.efetcher import Efetcher

usr_email = "liqiming1914658215@gmail.com"
api_key = "c80ce212c7179f0bbfbd88495a91dd356708"


def search():
    e = Esearcher('Esearch', usr_email, api_key)
    analyzer = e.inquire({'db': 'pubmed',
                          'term': 'Nature[ta]',
                          'sort': 'Date Released',
                          'mindate': '2019/05/01',
                          'maxdate': '2019/09/01',
                          'datetype': 'pdat',
                          'retmax': 10000}).result

    return analyzer.count, analyzer.uids


def eftch(idlist):
    e = Efetcher('Efetch', usr_email, api_key)
    analyzer = e.inquire({'db': 'pubmed',
                          'id': idlist,
                          'retmode': 'xml'}).get_result()
    return analyzer


def main():
    count, idlist = search()
    eftch(idlist)


if __name__ == '__main__':
    main()
