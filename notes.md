# Combinaisons

236 rimes différentes dans bd_rimes.json
788 sonnets
combinaisons de 5 dans les 236 (sans prise en compte du nb de vers dispos) : 1 767 738 973
`combis = combinaisons(range(len(type_rimes)), 5)`

Voir https://github.com/quadrismegistus/prosodic trouvé sur http://ryanheuser.org/sonnet-from-numbers/

# Requêtes SQL

Exemple : trouver 5 rimes riches où on trouve Rimbaud et Baudelaire

  * `select count(vers) as nb_vers, rime_riche, id_vers from tb_vers left join tb_sonnets on tb_vers.id_sonnet=tb_sonnets.id_sonnet where tb_sonnets.auteur = 'Arthur Rimbaud' or tb_sonnets.auteur='Paul Verlaine' group by tb_vers.rime_riche having nb_vers > 1 order by random() limit 5;`
Mais à on peut avoir que l'un ou que l'autre ou les deux auteurs.

  * Nombre de vers par rime
  `select rime_riche, count(*) as NUM from tb_vers where rime_riche != "" group by rime_riche order by count(*);`



