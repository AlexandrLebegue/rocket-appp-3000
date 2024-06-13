from openai import OpenAI
import streamlit as st
import hashlib

def generate_sha256_hash(text):
    # Encode le texte en bytes
    text_bytes = text.encode('utf-8')
    
    # Crée un objet SHA-256
    sha256 = hashlib.sha256()
    
    # Met à jour l'objet SHA-256 avec le texte encodé
    sha256.update(text_bytes)
    
    # Récupère le hachage en format hexadécimal
    hash_hex = sha256.hexdigest()
    
    return hash_hex

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("AstroTutos 🚀")
st.caption("L'astro pour les intellos 🤓")
cols =  st.columns(2)
with cols[0]:

    with st.expander("**Salutations, jeune avide de science intergalactique !** 👽", True): 
        st.write(""" Ce cours a pour mission de t'ouvrir les portes du vaste univers spatial.
                Si tu rêves de séduire Thomas Pesquet ou de devenir le premier à danser la Macarena sur Mars, 
                tu es au bon endroit ! Les interrogations qui te viennent quand tu lèves les yeux au ciel ? Oubliées ! 
                Alors, n'hésite plus et embarque pour ce cours cosmique. Bonne chance à toi, futur space addict ! 🌠""")
        


        st.image("https://static.hitek.fr/img/actualite/2017/02/27/w_couverture-facebook-biere-sur-la-lune-cosmonaute.webp")


with cols[1]:
    with st.expander("**Besoin d'aide ?** Le conseil de Toto, expert dans le domaine du spatial est là 🤖"):
        client = OpenAI(api_key=st.text_input("Entrer le mot de passe !"))
        if generate_sha256_hash(str(client.api_key)) == "ba2b2f49f5422567d42dc907c90cf9a666fceda9adb1b63dec90d71e1ff1c63b":
            st.success("Accès à l'oridnateur autorisé 🤖")
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])

            if prompt := st.chat_input("Ecrire ici si tu as une question 🤔"):
                st.session_state.messages.append({"role": "user", "content": prompt})
                with st.chat_message("user"):
                    st.markdown(prompt)

                with st.chat_message("assistant"):
                    stream = client.chat.completions.create(
                        model=st.session_state["openai_model"],
                        messages=[
                            {"role": m["role"], "content": m["content"]}
                            for m in st.session_state.messages
                        ],
                        stream=True,
                    )
                    response = st.write_stream(stream)
                st.session_state.messages.append({"role": "assistant", "content": response})
        else:
            st.write((generate_sha256_hash(str(client.api_key))))

with st.expander("Cours 1 : les orbites 🌍", True):
    st.subheader("**Bienvenue dans le monde merveilleux des orbites !**")
    st.caption("Promis, ce sera pas chiant 🪐")
    st.markdown(""" 
            Aujourd'hui nous allons comprendre comment fonctionne notre système solaire. 
            Voir ensemble les différents types d'orbites et voir même faire quelques maths ! Prêt ? C'est parti! 🚀
            """)
    
    st.subheader("**1. Qu'est-ce qu'une orbite ?** 🌍")
            
    st.markdown("""
            Imagine, tu es dans un champ. Dans ta main ? Un caillou. Oui, un caillou ordinaire. 
            Maintenant, tu décides de lancer ce caillou en l’air. Qu’est-ce qui se passe ? Eh bien, il retombe.
            Mais supposons que tu as un super bras (à la Hulk) et que tu lances ce caillou de plus en plus fort.
            À un moment, tu vas le lancer si fort qu’au lieu de retomber, il va commencer à faire le tour de la Terre.
            Félicitations, tu viens de créer une orbite !
            
            Quand tu lances ton caillou vraiment fort, il tombe constamment vers la Terre à cause de la gravité, 
            mais en raison de sa vitesse, il manque toujours le sol et continue de tourner autour de la planète. 
            **C’est ça, une orbite !**
                
            Tout simplement, les fusées utilisent le même principe pour se mettre en orbite. Elle décolle et monte très vite en altitude puis, là ou il n'y a pas de frottements elle oriente ses réacteurs de  manière à produire une poussée **tangeancielle** à la terre. On dit qu'elle **circularise** son orbite. Simple non ? 
            """)
                
    st.subheader("**2. Un peu d'histoire 📖**")

    st.markdown("""
            Les orbites ne sont pas nouvelles. Même les anciens Grecs en parlaient. 
                
            + Deux gars, **Aristote et Ptolémée** pensaient que tout tournait autour de la Terre. On appelle ça le **modèle Géocentrique**. Pour eux, la Terre est ronde et immobile et l'univers se divise en deux mondes. Celui qui se situe entre la Terre et la Lune est plutôt imprévisible. Celui que l'on trouve au-delà est régi par un ensemble de sphères concentriques qui évoluent à différentes vitesses et suivant des trajectoires circulaires parfaites.
            + Puis est arrivé **Copernic au XV - XVI Sciècle**, qui a dit "Euh, non, c’est plutôt la Terre qui tourne autour du Soleil.". Copernic est surtout connu pour avoir proposé le **modèle héliocentrique** du système solaire, dans lequel la Terre et les autres planètes tournent autour du Soleil. Cette idée était révolutionnaire à l'époque.
            + Ensuite, **Kepler** a débarqué avec ses lois pour mettre tout ça au carré (ou plutôt en ellipse mais on verra ça plus tard). Il est notamment très connu pour avoir formulé trois lois fondamentales qui décrivent le mouvement des planètes. 
                - **Première Loi (Loi des Orbites)** : Les planètes se déplacent sur des orbites elliptiques avec le Soleil à l'un des foyers.
                - **Deuxième Loi (Loi des Aires)** : Une ligne imaginaire reliant une planète au Soleil balaie des aires égales en des temps égaux, ce qui signifie que les planètes se déplacent plus rapidement lorsqu'elles sont plus proches du Soleil.
                - **Troisième Loi (Loi des Périodes)** : Le carré de la période orbitale d'une planète est proportionnel au cube de la distance moyenne de cette planète au Soleil (T² ∝ r³).   
            Ses travaux sont encore grandement utilisés de nos jours. 
        """)

    st.subheader("**3. Application dans la nature 🍃**")

    st.markdown("""      

            Les premiers exemples d'orbites dans la nature que nous rencontrons sont les mouvements des corps célestes. Les planètes, les lunes et même les astéroïdes suivent des trajectoires elliptiques ou circulaires autour du Soleil ou d'autres corps célestes. Ces orbites sont régies par les lois de Kepler et la gravitation, et elles influencent les saisons, les marées et d'autres phénomènes astronomiques.
            
            Au niveau cosmique, les étoiles, les systèmes binaires et même les galaxies peuvent être en orbite les unes autour des autres. Par exemple, notre Soleil orbite autour du centre de la Voie lactée, et la Voie lactée elle-même orbite autour d'autres galaxies dans l'Univers.
            
            Bref, dans notre univers, tout est en orbite autour de quelque chose.     
                    """)

    st.subheader("**4. Application par l'Homme 🤖**")
    
    st.markdown("""      

            Pourquoi les orbites sont-elles si cool ? Eh bien, sans elles, pas de satellites pour nous donner la météo, pas de GPS pour nous perdre moins souvent, et pas de selfies spatiaux de Thomas Pesquet. En gros, les orbites font en sorte que nos gadgets high-tech fonctionnent, et que nos astronautes ne finissent pas perdus dans l’espace comme dans un mauvais film de science-fiction.

            Nous verrons dans le chapitre 2 une description plus précise des différentes orbites utilisées par l'Homme 😉 Mais c'est l'heure de l'examen ! 
            """)
        
    st.subheader("**5. Place au questionnaire ! 📝**")

    st.markdown("""      
                
            Pour débloquer le chapitrer 2, il te faut réussir ce petit questionnaire qui résume ce que tu as appris plus haut ! Aie confiance en toi et bonne chance !😉 
            """)

    reponse = st.radio(
    "**1. Qu'est ce que le modèle géocentrique** ! ",
    ["Un modèle physique selon lequelle la phyisique la Terre est au centre de l'univers 🌍", "Un modèle physique selon lequelle la phyisique le Soleil est au centre de l'univers ☀️", "Un modèle selon lequelle les planètes tournent autours de la Lune 🌚"],
    index=None)

    
    st.write("Tu as choisi ", reponse)

    if reponse == "Un modèle physique selon lequelle la phyisique la Terre est au centre de l'univers 🌍":
        st.success("Bravo ! Question suivante !")

        reponse_2 = st.radio(
        "**2. Quelles sont les 3 lois formulées par Kepler** ? ",
        ["Loi de la Terre, Loi de la gravité, Loi des sphères", "Loi de la gravitation, Loi des deux corps, Loi des irrégularités", "Loi des Orbites, Loi des Aires, Loi des Périodes"],
        index=None)
        st.write("Tu as choisi ", reponse_2)
        
        if reponse_2 == "Loi des Orbites, Loi des Aires, Loi des Périodes":
            st.success("Encore bravo !! Question suivante !")

            reponse_3 = st.radio(
            "**2. Quelle technologie fonctionne grâce à la mise en orbite de sattelite** ? ",
            ["La 4G ! Partout et super rapide!", "Le GPS, pour savoir où on est !", "L'orbitron, un laser capable de chauffer et lisser les plis des vêtements automatiquements !"],
            index=None)
            st.write("Tu as choisi ", reponse_3)
            
            if reponse_3 == "Le GPS, pour savoir où on est !":
                st.success("Encore bravo !! Tu as réussi à terminer le cours numéro 1. Super simple non ? T'es pas prêt pour la suite 🥸")

if reponse and reponse_2 and reponse_3:
    st.success("Cours 2 débloqué ! Bravo à toi !")
    with st.expander("Cours 2 : Orbite artificielle et satellites 🛰️", True):
        st.subheader("**On approfondit un peu plus les différents types d'orbites 🛰️**")
                    
        st.markdown("""
                    Les satellites en orbite autour de la Terre sont un exemple moderne d'application des orbites dans la 
                    technologie spatiale. Ces objets artificiels sont placés dans des orbites spécifiques pour des missions 
                    de communication, d'observation de la Terre, de navigation GPS et bien plus encore. 
                    Comprendre les orbites est crucial pour leur placement et leur maintien en fonctionnement.
                    """)

        st.subheader("**1. Les différents types d'orbites 🌌**")
        
        st.markdown("""
                    Commençons par quelques types d'orbites couramment utilisées :
                    
                    + **Orbite basse terrestre (LEO)** : Ces orbites sont situées entre 160 km et 2 000 km d'altitude. Elles sont souvent utilisées pour les satellites d'observation de la Terre, les satellites espions et la Station Spatiale Internationale.
                    
                    + **Orbite géostationnaire (GEO)** : Située à environ 35 786 km au-dessus de l'équateur, cette orbite permet à un satellite de rester fixe par rapport à un point spécifique de la Terre. Elle est idéale pour les satellites de communication et météorologiques.
                    
                    + **Orbite polaire** : Ces orbites passent au-dessus des pôles Nord et Sud, permettant à un satellite de voir pratiquement toute la surface de la Terre au fil du temps. Elles sont parfaites pour les satellites d'observation globale.
                    """)
        
        st.subheader("**2. Les applications des différentes orbites 🚀**")
        
        st.markdown("""
                    + **Observation de la Terre et imagerie spatiale** : Les satellites en orbite basse (LEO) sont utilisés pour capturer des images haute résolution de la surface terrestre, ce qui est essentiel pour la cartographie, la surveillance environnementale et les applications militaires.
                    
                    + **Télécommunications** : Les satellites en orbite géostationnaire (GEO) jouent un rôle crucial dans les systèmes de télécommunications, permettant la diffusion de signaux télévisuels, la connectivité Internet et les communications de données à travers de vastes zones géographiques.
                    
                    + **Navigation GPS** : Les satellites en orbite moyenne terrestre (MEO), comme ceux du système GPS, permettent de fournir des services de positionnement, de navigation et de synchronisation pour des applications allant de la navigation automobile à l'aviation et à l'agriculture de précision.
                    """)

        st.subheader("**3. Comment placer un satellite en orbite ? 🌠**")
        
        st.markdown("""
                    Pour placer un satellite en orbite, plusieurs étapes sont nécessaires :
                    
                    + **Lancement** : Utilisation d'une fusée pour propulser le satellite en dehors de l'atmosphère terrestre.
                    
                    + **Insertion en orbite** : La fusée place le satellite sur une trajectoire initiale, souvent une orbite de transfert, qui l'amènera à son orbite finale.
                    
                    + **Mise à poste** : Utilisation de propulseurs embarqués pour ajuster l'orbite du satellite et le placer précisément à l'endroit souhaité.
                    
                    + **Opérations en orbite** : Surveillance et contrôle du satellite pour s'assurer qu'il reste en bonne santé et fonctionne comme prévu, y compris les ajustements d'orbite si nécessaire.
                    """)
        
        st.subheader("**4. Place au questionnaire ! 📝**")
        
        st.markdown("""
                    Pour débloquer le chapitre 3, il te faut réussir ce petit questionnaire qui résume ce que tu as appris plus haut ! Bonne chance ! 🚀
                    """)

        reponse_4 = st.radio(
            "**1. Quelle est l'altitude typique de l'orbite basse terrestre (LEO) ?** ",
            ["Entre 160 km et 2 000 km", "À environ 35 786 km", "Au-dessus des pôles"],
            index=None)
        st.write("Tu as choisi ", reponse_4)
        
        if reponse_4 == "Entre 160 km et 2 000 km":
            st.success("Bravo ! Question suivante !")

            reponse_5 = st.radio(
                "**2. Quelle orbite permet à un satellite de rester fixe par rapport à un point spécifique de la Terre ?** ",
                ["Orbite basse terrestre (LEO)", "Orbite géostationnaire (GEO)", "Orbite polaire"],
                index=None)
            st.write("Tu as choisi ", reponse_5)
            
            if reponse_5 == "Orbite géostationnaire (GEO)":
                st.success("Encore bravo !! Question suivante !")

                reponse_6 = st.radio(
                    "**3. Quel type de satellite utilise généralement une orbite moyenne terrestre (MEO) ?** ",
                    ["Satellite d'observation de la Terre", "Satellite de télécommunications", "Satellite GPS"],
                    index=None)
                st.write("Tu as choisi ", reponse_6)
                
                if reponse_6 == "Satellite GPS":
                    st.success("Encore bravo !! Tu as réussi à terminer le cours numéro 2. Bien joué ! Prépare-toi pour le cours numéro 3 !")

if reponse_4 and reponse_5 and reponse_6:
    st.success("Cours 3 débloqué ! Bravo à toi !")
    with st.expander("Cours 3 : Les lois de la gravitation 🌌", True):
        st.subheader("**Plongeons dans les lois de la gravitation !**")
                    
        st.markdown("""
                    Maintenant que tu sais ce qu'est une orbite et comment l'utiliser, il est temps de comprendre pourquoi les choses se déplacent en orbite. Nous allons explorer les lois de la gravitation qui régissent le mouvement des objets dans l'espace.
                    """)
                    
        st.subheader("**1. La loi de la gravitation universelle de Newton**")
        
        st.markdown("""
                    + **Isaac Newton** a formulé la loi de la gravitation universelle, qui décrit comment deux objets s'attirent mutuellement avec une force qui dépend de leurs masses et de la distance qui les sépare.
                    
                    + La formule est : **F = G * (m1 * m2) / r²**, où :
                        - **F** est la force de gravité entre les deux objets,
                        - **G** est la constante gravitationnelle,
                        - **m1** et **m2** sont les masses des deux objets,
                        - **r** est la distance entre les centres des deux objets.
                    """)
                    
        st.subheader("**2. Les applications de la gravitation**")
        
        st.markdown("""
                    + **Mouvement des planètes** : La gravitation maintient les planètes en orbite autour du Soleil.
                    
                    + **Marées** : La gravitation de la Lune provoque les marées sur Terre.
                    
                    + **Structures galactiques** : La gravitation maintient ensemble les étoiles et les galaxies.
                    """)
        
        st.subheader("**3. La gravité et les trajectoires orbitales**")
        
        st.markdown("""
                    + **Vitesse orbitale** : La vitesse à laquelle un objet doit se déplacer pour rester en orbite autour d'un autre objet est déterminée par la gravité. Cette vitesse dépend de la masse de l'objet central et de la distance de l'objet en orbite.
                    
                    + **Transferts orbitaux** : Pour changer d'orbite, un objet doit modifier sa vitesse en utilisant des propulseurs. Ces manœuvres utilisent les principes de la gravitation pour atteindre de nouvelles orbites.
                    """)
        
        st.subheader("**4. Place au questionnaire ! 📝**")
        
        st.markdown("""
                    Pour débloquer le chapitre 4, il te faut réussir ce petit questionnaire qui résume ce que tu as appris plus haut ! Bonne chance ! 🌠
                    """)

        reponse_7 = st.radio(
            "**1. Qui a formulé la loi de la gravitation universelle ?** ",
            ["Albert Einstein", "Isaac Newton", "Galileo Galilei"],
            index=None)
        st.write("Tu as choisi ", reponse_7)
        
        if reponse_7 == "Isaac Newton":
            st.success("Bravo ! Question suivante !")

            reponse_8 = st.radio(
                "**2. Quelle est la formule de la force gravitationnelle entre deux objets ?** ",
                ["F = m1 * m2 / r", "F = G * (m1 * m2) / r²", "F = G * m1 * m2 * r²"],
                index=None)
            st.write("Tu as choisi ", reponse_8)
            
            if reponse_8 == "F = G * (m1 * m2) / r²":
                st.success("Encore bravo !! Question suivante !")

                reponse_9 = st.radio(
                    "**3. Quelle force provoque les marées sur Terre ?** ",
                    ["La gravité du Soleil", "La gravité de la Lune", "La force centrifuge"],
                    index=None)
                st.write("Tu as choisi ", reponse_9)
                
                if reponse_9 == "La gravité de la Lune":
                    st.success("Encore bravo !! Tu as réussi à terminer le cours numéro 3. Bien joué ! Prépare-toi pour le cours numéro 4 !")