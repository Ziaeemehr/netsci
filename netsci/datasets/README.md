# DATABASES

## Network Datasets

Nodes are labelled from 0 continuously. Each line contains contains two node labels A and B, representing either a directed link A->B or an undirected link A-B. Undirected links appear once in the file.


1) Actor:
Based on 2004 imdb data. Nodes represent actors, two nodes are connected if the corresponding actors made at least one movie together. Made for TV, direct-to-video and video game entries were removed. Preprocessed data courtesy of Hawoong Jeong.

2) Collaboration:
Scientific collaboration network based on the arXiv preprint archive's Condense Matter Physics category covering the period from January 1993 to April 2003. Each node represents an author, and two nodes are connected if they co-authored at least one paper in the dataset. Ref: Leskovec, J., Kleinberg, J., & Faloutsos, C. (2007). Graph evolution: Densification and shrinking diameters. ACM Transactions on Knowledge Discovery from Data (TKDD), 1(1), 2.

3) Internet
Network of routers connected to each other compiled by the Center for Applied Internet Data Analysis (CAIDA). Nodes are routers, and they are connected if they are directly connected via cables. For details of the non-trivial task of collecting the data see the reference. Ref: http://www.caida.org/tools/measurement/skitter/router_topology/

4) Power Grid
Network representing the Western States Power Grid of the United States. Each node is a power plant, transformer or consumer, and two nodes are connected if they are physically connected via a cable. Ref: Watts, D. J., & Strogatz, S. H. (1998). Collective dynamics of â€˜small-worldâ€™ networks. nature, 393(6684), 440-442.

5) Protein
Network representing the protein-protein interactions in yeast. Each node represents a protein, and they are connected if they physically interact within the cell. Original data: http://interactome.dfci.harvard.edu/S_cerevisiae/index.php?page=download Ref: Yu, H., Braun, P., YÄ±ldÄ±rÄ±m, M. A., Lemmens, I., Venkatesan, K., Sahalie, J., ... & Vidal, M. (2008). High-quality binary protein interaction map of the yeast interactome network. Science, 322(5898), 104-110.

6) Phone Calls:
Nodes represent a sample of cell phone users, they are connected if they have called each other at least once during the observed period. Data set contains a subset of most active users from (Song et al, 2010). Data provided by Chaoming Song. Ref: Song, C., Qu, Z., Blumm, N., & BarabÃ¡si, A. L. (2010). Limits of predictability in human mobility. Science, 327(5968), 1018-1021.

7) Citation:
Citation network of the APS journals (Physical Review Letters, Physical Review, and Reviews of Modern Physics). Each node represents a paper, and there is a directed link connecting node A to node B, if A cites B. Original data: http://journals.aps.org/datasets Details: Redner, S. (2004). Citation statistics from more than a century of physical review. arXiv preprint physics/0407137.

8) Metabolic
Network representing the metabolic reactions of the E. coli bacteria. Each node is a metabolite, and each directed link A->B means that there is a reaction where A is an input and B is a product (e.g. A+C -> B+D). Original data: http://bigg.ucsd.edu/ Ref: Schellenberger, J., Park, J. O., Conrad, T. M., & Palsson, B. Ã˜. (2010). BiGG: a Biochemical Genetic and Genomic knowledgebase of large scale metabolic reconstructions. BMC bioinformatics, 11(1), 213.

9) Email:
Email network based on traffic data collected for 112 days at University of Kiel, Germany. Each node is an email address, and there is a directed link from node A to node B, if A sent at least one email to B. Ref: Ebel, H., Mielsch, L. I., & Bornholdt, S. (2002). Scale-free topology of e-mail networks. Physical review E, 66(3), 035103.

10) WWW
Nodes represent web pages form the University of Notre Dame under the domain nd.edu, directed links represent hyperlinks between them. Data collected in 1999. Ref: Albert, R., Jeong, H., & BarabÃ¡si, A. L. (1999). Internet: Diameter of the world-wide web. Nature, 401(6749), 130-131.


#### References

- [String](https://string-db.org/)
- [Network Databases, Barabasi book](https://networksciencebook.com/translations/en/resources/data.html)