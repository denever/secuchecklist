# -*- coding: utf-8 -*

PHONE_CHOICES = (
    '02', #Milano
    '06', #Roma
    '010', #Genova
    '011', #Torino
    '015', #Biella
    '019', #Savona
    '030', #Brescia
    '031', #Como
    '035', #Bergamo
    '039', #Monza
    '040', #Trieste
    '041', #Venezia (Mestre)
    '045', #Verona
    '049', #Padova
    '050', #Pisa
    '051', #Bologna
    '055', #Firenze
    '059', #Modena
    '070', #Cagliari
    '071', #Ancona
    '075', #Perugia
    '079', #Sassari
    '080', #Bari
    '081', #Napoli
    '085', #Pescara
    '089', #Salerno
    '090', #Messina
    '091', #Palermo
    '095', #Catania
    '099', #Taranto
    '0121', #Pinerolo
    '0122', #Susa
    '0123', #Lanzo Torinese
    '0124', #Rivarolo Canavese
    '0125', #Ivrea
    '0131', #Alessandria
    '0141', #Asti
    '0142', #Casale Monferrato
    '0143', #Novi Ligure
    '0144', #Acqui Terme
    '0161', #Vercelli
    '0163', #Borgosesia
    '0165', #Aosta
    '0166', #St.Vincent
    '0171', #Cuneo
    '0172', #Savigliano
    '0173', #Alba
    '0174', #Mondovì
    '0175', #Saluzzo
    '0182', #Albenga
    '0183', #Imperia
    '0184', #San Remo
    '0185', #Rapallo
    '0187', #La Spezia
    '0321', #Novara
    '0322', #Arona
    '0323', #Baveno
    '0324', #Domodossola
    '0331', #Busto Arsizio
    '0332', #Varese
    '0341', #Lecco
    '0342', #Sondrio
    '0343', #Chiavenna
    '0344', #Menaggio
    '0345', #S.Pellegrino Terme
    '0346', #Clusone
    '0362', #Seregno
    '0363', #Treviglio
    '0364', #Breno
    '0365', #Salò
    '0371', #Lodi
    '0372', #Cremona
    '0373', #Crema
    '0374', #Soresina
    '0375', #Casalmaggiore
    '0376', #Mantova
    '0377', #Codogno
    '0381', #Vigevano
    '0382', #Pavia
    '0383', #Voghera
    '0384', #Mortara
    '0385', #Stradella
    '0386', #Ostiglia
    '0421', #S.Donà di Piave
    '0422', #Treviso
    '0423', #Montebelluna
    '0424', #Bassano del Grappa
    '0425', #Rovigo
    '0426', #Adria
    '0427', #Spilimbergo
    '0428', #Tarvisio
    '0429', #Este
    '0431', #Cervignano del Friuli
    '0432', #Udine
    '0433', #Tolmezzo
    '0434', #Pordenone
    '0435', #Pieve di Cadore
    '0436', #Cortina d'Ampezzo
    '0438', #Conegliano
    '0439', #Feltre
    '0442', #Legnago
    '0444', #Vicenza
    '0445', #Schio
    '0461', #Trento
    '0462', #Cavalese
    '0463', #Cles
    '0464', #Rovereto
    '0465', #Tione di Trento
    '0471', #Bolzano
    '0472', #Bressanone
    '0437', #Belluno
    '0473', #Merano
    '0474', #Brunico
    '0481', #Gorizia
    '0521', #Parma
    '0522', #Reggio nell'Emilia
    '0523', #Piacenza
    '0524', #Fidenza
    '0525', #Fornovo di Taro
    '0532', #Ferrara
    '0533', #Comacchio
    '0534', #Porretta Terme
    '0535', #Mirandola
    '0536', #Sassuolo
    '0541', #Rimini
    '0542', #Imola
    '0543', #Forlì
    '0544', #Ravenna
    '0545', #Lugo
    '0546', #Faenza
    '0547', #Cesena
    '0549', #S.Marino (Rep. di)
    '0564', #Grosseto
    '0565', #Piombino
    '0566', #Follonica
    '0571', #Empoli
    '0572', #Montecatini Terme
    '0573', #Pistoia
    '0574', #Prato
    '0575', #Arezzo
    '0577', #Siena
    '0578', #Chianciano Terme
    '0583', #Lucca
    '0584', #Viareggio
    '0585', #Massa
    '0586', #Livorno
    '0587', #Pontedera
    '0588', #Volterra
    '0721', #Pesaro
    '0722', #Urbino
    '0731', #Jesi
    '0732', #Fabriano
    '0733', #Macerata
    '0734', #Fermo
    '0735', #S.Benedetto del Tronto
    '0736', #Ascoli Piceno
    '0737', #Camerino
    '0742', #Foligno
    '0743', #Spoleto
    '0744', #Terni
    '0746', #Rieti
    '0761', #Viterbo
    '0763', #Orvieto
    '0765', #Poggio Mirteto
    '0766', #Civitavecchia
    '0771', #Formia
    '0773', #Latina
    '0774', #Tivoli
    '0775', #Frosinone
    '0776', #Cassino
    '0781', #Iglesias
    '0782', #Lanusei
    '0783', #Oristano
    '0784', #Nuoro
    '0785', #Macomer
    '0789', #Olbia
    '0823', #Caserta
    '0824', #Benevento
    '0825', #Avellino
    '0827', #S.Angelo dei Lombardi
    '0828', #Battipaglia
    '0831', #Brindisi
    '0832', #Lecce
    '0833', #Gallipoli
    '0835', #Matera
    '0836', #Maglie
    '0861', #Teramo
    '0862', #L'Aquila
    '0863', #Avezzano
    '0864', #Sulmona
    '0865', #Isernia
    '0871', #Chieti
    '0872', #Lanciano
    '0873', #Vasto
    '0874', #Campobasso
    '0875', #Termoli
    '0881', #Foggia
    '0882', #San Severo
    '0883', #Andria
    '0884', #Manfredonia
    '0885', #Cerignola
    '0921', #Cefalù
    '0922', #Agrigento
    '0923', #Trapani
    '0924', #Alcamo
    '0925', #Sciacca
    '0931', #Siracusa
    '0932', #Ragusa
    '0933', #Caltagirone
    '0934', #Caltanissetta
    '0935', #Enna
    '0941', #Patti
    '0942', #Taormina
    '0961', #Catanzaro
    '0962', #Crotone
    '0963', #Vibo Valentia
    '0964', #Locri
    '0965', #Reggio di Calabria
    '0966', #Palmi
    '0967', #Soverato
    '0968', #Lamezia Terme
    '0971', #Potenza
    '0972', #Melfi
    '0973', #Lagonegro
    '0974', #Vallo della Lucania
    '0975', #Sala Consilina
    '0976', #Muro Lucano
    '0981', #Castrovillari
    '0982', #Paola
    '0983', #Rossano
    '0984', #Cosenza
    '0985'  #Scalea
)

MOBILE_CHOICES = ( 
    '330', #TIM
    '331', #TIM
    '333', #TIM
    '334', #TIM
    '335', #TIM
    '336', #TIM
    '337', #TIM
    '338', #TIM
    '339', #TIM
    '360', #TIM
    '363', #TIM
    '366', #TIM
    '368', #TIM

    '340', #Vodafone Italia 
    '342', #Vodafone Italia
    '345', #Vodafone Italia
    '346', #Vodafone Italia
    '347', #Vodafone Italia
    '348', #Vodafone Italia
    '349', #Vodafone Italia

    '320', #Wind 
    '323', #Wind
    '327', #Wind
    '328', #Wind
    '329', #Wind
    '380', #Wind
    '383', #Wind
    '388', #Wind
    '389', #Wind

    '390', #3 Italia 
    '391', #3 Italia
    '392', #3 Italia
    '393', #3 Italia

    '377', #BT Mobile (Vodafone)
    '373', #Fastweb (3 Italia)
    '370'  #Tiscali (TIM)
)
