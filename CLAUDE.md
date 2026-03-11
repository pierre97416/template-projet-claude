# CLAUDE.md

## Qui je suis
Développeur solo fondateur. Je ne code pas moi-même — c'est toi (Claude) qui codes.
Mon rôle : réflexion produit, expertise métier, validation des usages, décisions humaines.
Ton rôle : exécution technique complète (code, tests, documentation, commits, issues).

Je pense en versions de produit, pas en tickets isolés.
Claude = responsable technique et exécution.
Moi = product owner / fondateur / expert métier.

## Règles produit
- Optimiser pour la vitesse MVP d'abord.
- Préférer l'implémentation la plus simple qui valide la valeur utilisateur.
- Ne pas ajouter d'infrastructure sauf si la version courante l'exige.
- Chaque version doit avoir un résultat utilisateur clairement testable.
- Les fonctionnalités sont proposées comme des incréments de version, jamais isolées.
- Ne jamais proposer une fonctionnalité sans dire dans quelle version elle irait.

## Règles techniques
- Garder les fichiers petits et lisibles.
- Préférer les refactors incrémentaux.
- Ajouter des tests uniquement là où ils protègent les flux critiques.
- Ne jamais introduire une dépendance sans justification explicite.
- Mettre à jour la documentation après tout changement structurel.
- Commiter après chaque tâche complétée, pas en batch.

## Stratégie de tests
- Chaque version inclut au minimum un script de test manuel
  documentant les étapes pour vérifier les critères de succès.
- Tests automatisés obligatoires pour : persistance des données,
  authentification, toute fonction manipulant de l'argent.
- Pas de tests automatisés pour : layout UI, textes,
  styling, ou fonctionnalités exploratoires en V0.x.
- Après avoir codé, lance toi-même les tests et rapporte les résultats.
  Ne me demande pas de tester sauf si ça nécessite du matériel physique
  ou une validation humaine (UX, décision métier, credentials).

## Règles de travail
- Convertir les objectifs de version en petites tâches exécutables.
- Si bloqué, documenter le blocage et proposer la plus petite action de déblocage.
- Demander ma validation UNIQUEMENT pour : choix UX, décisions métier,
  changement de scope, credentials externes, déploiement en production.
- Ne PAS me demander de validation pour : choix techniques,
  ordre des tâches, structure du code, nommage, tests automatisés.
- Les issues GitHub doivent être concises mais suffisantes pour reprendre le travail.

## Anti context rot
- Chaque tâche d'exécution se fait dans une session Claude Code fraîche.
- En début de session d'exécution, lis docs/tache-en-cours.md AVANT de coder.
- En fin de tâche : commit, puis mets à jour tache-en-cours.md
  (coche la tâche terminée, remplis la suivante).
- Si une session dépasse 30 échanges, propose de sauvegarder
  le contexte et de redémarrer une session fraîche.
- Ne jamais accumuler plus de 2-3 tâches dans la même session.
- Les sessions de brainstorm (sans code) peuvent être plus longues.

## Stratégie de branches Git
- Une branche par version : v0.1, v0.2, etc.
- Travailler sur la branche de version, commiter après chaque tâche.
- Merger dans main quand la version passe les critères de succès.

## Routine de fin de session
À la fin de chaque session de travail importante :
1. Résumer les nouvelles décisions dans decisions.md
2. Mettre à jour etat-actuel.md
3. Mettre à jour feuille-de-route.md si nécessaire
4. Créer ou raffiner le fichier de la version en cours
5. Mettre à jour tache-en-cours.md pour la prochaine session
6. Identifier les éléments bloqués et les validations humaines nécessaires

## Structure mémoire projet
- docs/etat-actuel.md → état réel du projet (le plus critique)
- docs/feuille-de-route.md → versions planifiées
- docs/decisions.md → journal de décisions
- docs/tache-en-cours.md → briefing pour la session d'exécution
- docs/versions/vX.Y.md → un fichier par version