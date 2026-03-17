# Surpreenda seus colegas!
meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKER": "Investigar a vida de alguém online",
            "FLOP": "Usado para descrever algo que não teve sucesso ou que falhou",
            "NPC": "meu date só falava de whey protein e dizia 'top'. um npc de academia total.",
            "VIBE": "esse rolê aqui tá vibes boas.",
            "MEME PRONTO": "ele tropeçou, caiu na escada e ainda soltou um ‘tô bem’. meme pronto demais.",
            "EMOJI HUMANO": "ela tem a mesma energia do 😭 em tempo integral. emoji humano real.",
            "POV": "POV: você tentando parecer tranquilo enquanto seu crush posta story com outro.",
            "VIRALIZAR": "postei um vídeo do meu vô dançando calypso e viralizou em 6 horas.",
            "TREND": "essa trend de colocar a cara do namorado no corpo do Ken já deu, hein.",
            }

word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")

if word in meme_dict.keys():
    meme = meme_dict[word]
    print(meme)
else:
    print("item não encontrado")
