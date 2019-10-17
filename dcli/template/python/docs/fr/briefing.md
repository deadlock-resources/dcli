# Détecteur de Spam

La fouille de données consiste en l'extraction de connaissances à partir d'une grande quantité de données en mettant en place des méthodes automatiques ou semi-automatiques.
Afin de réaliser ceci, on utilise un algorithme tiré de différentes disciplines scientifiques tel que les statistiques, l'intelligence artificielle ou bien de l'informatique.
Le but est de construire un modèle et d'extraire le plus de connaissances possibles depuis les données fournies en respectant des critères.

Dans cette mission, vous allez mettre en place un algorithme que vous allez **entrainer** à détecter des messages spam.

Voici les librairies que vous allez utiliser dans cette mission :

* La librairie Scipy et spécifiquement la classe  [ttest_ind](https : //docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)
* [Librairie Numpy](http : //www.numpy.org/)
* Algorithm TF-IDF, vous devez utiliser les attributs  _stop_mots_="english"  et _min_df_ =0.0005. (cela permet d'enlever les mots qui n'ont pas de sens sémantiques tels que : me, you, the...)

Voici la documentation de l'algorithme TF-IDF  :  <https : //scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html>

Voici un exemple sur le fonctionnement de l'algorithme TF-IDF :
Nous allons prendre trois phrases comme exemple.
   1ère phrase   :   Bonjour, j'aime chats  
   2ème phrase   :   Bonjour, j'aime chiens
   3ème phrase   :   Cette phrase contient ce texte
***TF***  :  Term Frequencies, la fréquence à laquelle un mot est présent dans une phrase.
   $$ TF(mot,phrase) = {|mot \in phrase| \over |phrase|}.$$

***IDF***  :  Inverse Document Frequencies
$$ IDF(mot) = ln({N \over |mot \in sen|}).$$
i.e. le nombre total de phrases (ici 3) sur le nombre de fois qu'un mot apparait dans différentes phrases.
(ici Bonjour apparait dans deux phrases).

L'encodage (les 1/4, 1/5 représentent l'encodage IF) :
 |   | j'  | aime  | chats  | chiens  | document  | bonjour  | ce | texte  | contient  |
 |---|---|---|---|---|---|---|---|---|---|
 | 1ére phrase  | 1/4   |  1/4  |  1/4  |  0 | 0  | 1/4   | 0  | 0  | 0  |
 | 2éme phrase  | 1/4   | 1/4   | 0  | 1/4   |  0 |  1/4  |  0 |  0 |  0 |
 | 3éme phrase  |  0 | 0  | 0  | 0  | 1/5  | 0  | 2/5  | 1/5  | 1/5  |
 |    IDF       | 0.4 | 0.4 | 1.09 | 1.09 | 1.09 | 0.4 | 1.09 |1.09 | 1.09 |

***TF-IDF*** final :
$$ TF-IDF(mot,phrase) = TF(mot,phrase) \times IDF(mot) .$$
 |   | j'  | aime  | chats  | chiens  | document  | bonjour  | ce | texte  | contient  |
 |---|---|---|---|---|---|---|---|---|---|
 | 1ére phrase  | 0.1 | 0.1 |  0.273  |  0 | 0  | 0.1   | 0  | 0  | 0  |
 | 2éme phrase  | 0.1 | 0.1 | 0  | 0.273   |  0 |  0.1  |  0 |  0 |  0 |
 | 3éme phrase  |  0  |  0  | 0  | 0  | 0.218  | 0  | 0.44  | 0.218  | 0.218  |

Au final vous obtenez un _term-document matrix_ où chaque (i , j) représente la fréquence du terme i dans la phrase j.

**Revenons à nos moutons** :

Dans cet exercice vous devez classifier les mots par ordre de "discriminative power" à partir de tests statistiques.
On vous fournit un fichier _spam.dms_ que vous allez utiliser, il contient des messages de type spam et des messages de type non-spam. Chaque ligne est rédigée comme suit :

    spam	+123 Congratulations - in this week's competition draw u have won the $1450 prize to claim just call 09050002311 b4280703 
    text     Is that seriously how you spell his name?  

Ce que vous devez faire :

1 - Extraire les données depuis le fichier _spam.dms_ et retourner une matrice qui contient des messages en TF-IDF et un vecteur (1 si spam and 0 sinon)

_Dans la TF-IDF documentation vous trouverez des méthodes qui vont vous aider à recupérer la term-document matrice, vous devez choisir la bonne méthode._
_Afin de convertir votre liste de 0 et 1 en vecteur vous pouvez utiliser la librairie Numpy_

``` python
    def transform_text(pairs) :
        return (matrix, vector)

```

   ***pairs*** est la liste des tuples(message, type) (type peut être spam ou text)

2 - Vous devez coder une méthode qui pour chaque mot renvoie sa p-value.
    Une p-value est la probabilité que le mot ne soit PAS surreprésenté dans les spams. Plus la valeur p est petite,
        plus le mot est surreprésenté dans les spams par rapport au non spam (texte).

_La matrice étant une matrice creuse vous devez la convertir en une matrice "dense" i.e. ne contient pas de zéros. Vous devez utiliser une méthode de la librairie Scipy._

   ``` python
        def mot_pvalue(matrix, vector, mot_pos) :
            return pvalue
  ```

  ***mot_pos*** represente un entier dans la matrice.