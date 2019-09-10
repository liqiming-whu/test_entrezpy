import entrezpy.conduit
c = entrezpy.conduit.Conduit('liqiming1914658215@gmail')
fetch_influenza = c.new_pipeline()
sid = fetch_influenza.add_search({'db': 'pubmed',
                                  'term': 'nature[ta]',
                                  'rettype': 'uilist',
                                  'sort': 'Date Released',
                                  'mindate': '2019/05/01',
                                  'maxdate': '2019/09/01',
                                  'datetype': 'pdat'})
fid = fetch_influenza.add_fetch({'retmax': 10000, 'retmode': 'xml'},
                                dependency=sid)
c.run(fetch_influenza)
