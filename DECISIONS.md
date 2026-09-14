# Décisions

Journal des décisions techniques du projet. Une entrée par décision : ce qui a été
décidé, pourquoi, et ce que j'ai écarté. Écrit avant le code, mis à jour si une
décision change.

---

## 2026-08-31 | Python, pas N8N ni JavaScript

**Décision.** Je construis la v1 en Python, alors que je n'ai jamais codé en Python
avant ce projet.

**Pourquoi.** Le but de ce projet, c'est de montrer que je sais coder. Si je le fais
en N8N, ça prouve surtout que je sais faire du no-code — ce qui est exactement
l'inverse de ce que je veux montrer. En plus, Python c'est le langage des postes que
je vise, donc le temps passé à l'apprendre n'est pas du temps perdu, c'est un
investissement direct.

**Écarté.** Faire une v1 rapide en JS ou N8N, puis la réécrire en Python pour la v2.
Ça irait plus vite à livrer, mais tout ce travail serait à refaire, et l'outil livré
en premier n'enverrait pas le bon signal.

---

## 2026-08-31 | Les règles détectent, le LLM synthétise — jamais l'inverse

**Décision.** Toute la détection d'anomalies passe par des règles écrites en dur
(email, âge, téléphone...). Le LLM ne sert qu'à regrouper et résumer ce que ces
règles ont déjà trouvé — il ne détecte rien lui-même.

**Pourquoi.** Un audit doit donner le même résultat à chaque fois sur les mêmes
données, et je dois pouvoir expliquer pourquoi une ligne est signalée. Un LLM à qui
on demande de repérer des anomalies ne va pas forcément trouver la même chose deux
fois, et je ne peux pas garantir qu'il ne loupe rien. J'ai eu la preuve concrète du
problème en testant : demandé au LLM de compter des anomalies par type à partir
d'une liste, il a ajouté +1 à chaque catégorie, de façon cohérente mais fausse. Ça
confirme que compter/détecter, ce n'est pas son rôle ici — la synthèse et la mise en
forme, oui.

**Écarté.** Envoyer le CSV brut au LLM et lui demander de trouver les problèmes
lui-même. Plus simple à coder, mais pas fiable, et invendable devant un client ou un
recruteur qui demanderait "comment tu garantis que ça détecte tout ?".

---

## 2026-08-31 | Périmètre v1 volontairement minimal

**Décision.** La v1 c'est : CSV en entrée, règles de validation, un appel LLM pour
la synthèse, rapport en Markdown en sortie. Rien de plus pour l'instant.

**Pourquoi.** Chaque brique en plus que je ne maîtrise pas encore (base de données,
observabilité, Docker...) augmente le risque de ne rien avoir de fini pour la
deadline. Un petit outil qui marche vaut mieux qu'un gros projet à moitié construit.

**Volontairement hors scope pour la v1.** Base de données, Supabase, observabilité
type Langfuse, plusieurs modèles LLM, Docker, interface web, recherche vectorielle.
Ce sont des pistes pour une v2, une fois la v1 terminée et solide.

---

## 2026-08-31 | Données de test 100% inventées

**Décision.** J'utilise un CSV de clients fictifs, avec des anomalies que j'ai
injectées volontairement (email sans @, âge négatif ou hors plage, téléphone mal
formaté...).

**Pourquoi.** Je n'ai pas accès à de vraies données CRM pour l'instant, et même si
j'en avais, je ne pourrais pas les utiliser pour un projet public (confidentialité).
Inventer les données a un avantage en plus : je connais à l'avance les anomalies
que j'ai mises, donc je peux vérifier que mon code les détecte toutes — ça sert de
test.
