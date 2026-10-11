import asyncio
from sqlalchemy import select
from .db.session import async_SessionLocal, create_table, engine
from .models.collection import Collection  
from .models.item import Items
from .models.user import Users 

CATALOGUE = [
    ("Age of Empires", "rts", "Des civilisations evoluent de l'Antiquite a l'age du fer.", 1997, "Ensemble Studios", "Rick Goodman", "https://static.wikia.nocookie.net/ageofempires/images/c/c4/Age_of_Empires_logo.png/revision/latest?cb=20150420140731&path-prefix=fr"),
    ("Age of Empires II: The Age of Kings", "rts", "Des civilisations medievales se disputent la domination.", 1999, "Ensemble Studios", "Bruce Shelley", "https://static.wikia.nocookie.net/ageofempires/images/c/cc/AoE2DE_logo.png/revision/latest/scale-to-width-down/1000?cb=20250227112959&path-prefix=fr"),
    ("Age of Empires IV", "rts", "Des civilisations historiques s'affrontent au Moyen Age.", 2021, "Relic Entertainment", "Adam Isgreen", "https://static.wikia.nocookie.net/ageofempires/images/1/12/Logo-age4-vert-1.png/revision/latest?cb=20170821203233"),
    ("Age of Mythology", "rts", "Des dieux et des creatures mythiques s'invitent dans la guerre.", 2002, "Ensemble Studios", "Greg Street", "https://static.wikia.nocookie.net/ageofempires/images/e/e0/Logo_AoMR.png/revision/latest/scale-to-width-down/1000?cb=20240609182923"),
    ("Anno 1602", "gestion", "Des colons developpent des iles et commercent en mer.", 1998, "Max Design", "Wilfried Reiter", "https://thumb.wikimedia.org/wikipedia/fr/thumb/2/23/Anno_1602_Logo.png/250px-Anno_1602_Logo.png?utm_source=fr.wikipedia.org&utm_campaign=parser&utm_content=thumbnail"),
    ("Baldur's Gate", "rpg", "Une aventure de role dans les Royaumes oublies.", 1998, "BioWare", "James Ohlen", "https://fr.wikipedia.org/wiki/Fichier:Baldur's_Gate_Logo.png"),
    ("Baldur's Gate II: Shadows of Amn", "rpg", "Le heros de Baldur's Gate affronte le mage Jon Irenicus.", 2000, "BioWare", "James Ohlen", "https://thumb.wikimedia.org/wikipedia/fr/thumb/6/62/Baldur%27s_Gate_II_Shadows_of_Amn_Logo.png/250px-Baldur%27s_Gate_II_Shadows_of_Amn_Logo.png?utm_source=fr.wikipedia.org&utm_campaign=parser&utm_content=thumbnail"),
    ("Baldur's Gate 3", "rpg", "Des aventuriers infectes par un parasite mental cherchent un remede.", 2023, "Larian Studios", "Swen Vincke", "https://thumb.wikimedia.org/wikipedia/fr/thumb/d/dc/Baldur%27s_Gate_III_Logo.png/250px-Baldur%27s_Gate_III_Logo.png?utm_source=fr.wikipedia.org&utm_campaign=parser&utm_content=thumbnail"),
    ("BioShock", "fps", "Un survivant explore la cite sous-marine de Rapture.", 2007, "2K Boston", "Ken Levine", ""),
    ("Borderlands 2", "fps", "Des chasseurs de l'Arche explorent Pandora.", 2012, "Gearbox Software", "Paul Sage", ""),
    ("Caesar III", "gestion", "Un gouverneur fait prosperer une cite de l'Empire romain.", 1998, "Impressions Games", "Simon Bradbury", ""),
    ("Call of Duty 4: Modern Warfare", "fps", "Des soldats menent des operations modernes.", 2007, "Infinity Ward", "Mackey McCandlish", ""),
    ("Cities: Skylines", "gestion", "Une metropole est planifiee et developpee.", 2015, "Colossal Order", "Mariina Hallikainen", ""),
    ("Command & Conquer", "rts", "Le GDI et le Nod se disputent le controle du Tiberium.", 1995, "Westwood Studios", "Brett Sperry", ""),
    ("Command & Conquer: Generals", "rts", "Les Etats-Unis, la Chine et la GLA s'affrontent dans un conflit moderne.", 2003, "EA Pacific", "Mike Verdu", ""),
    ("Command & Conquer: Red Alert", "rts", "Les Allies et les Sovietiques s'affrontent dans une histoire alternative.", 1996, "Westwood Studios", "Brett Sperry", ""),
    ("Company of Heroes", "rts", "Des troupes alliees combattent en Europe pendant la Seconde Guerre mondiale.", 2006, "Relic Entertainment", "Quinn Duffy", ""),
    ("Company of Heroes 2", "rts", "Les Sovietiques affrontent la Wehrmacht sur le front de l'Est.", 2013, "Relic Entertainment", "Quinn Duffy", ""),
    ("Counter-Strike", "fps", "Deux equipes s'affrontent dans des missions tactiques.", 2000, "Valve", "Minh Le", ""),
    ("Dark Souls III", "rpg", "Un Morteflamme explore un royaume en ruines.", 2016, "FromSoftware", "Hidetaka Miyazaki", ""),
    ("Deus Ex", "rpg", "Un agent augmente enquete sur un complot mondial.", 2000, "Ion Storm", "Warren Spector", ""),
    ("Diablo II", "rpg", "Des heros affrontent les seigneurs des Enfers.", 2000, "Blizzard North", "David Brevik", ""),
    ("Disco Elysium", "rpg", "Un detective amnesique enquete dans la ville de Revachol.", 2019, "ZA/UM", "Robert Kurvitz", ""),
    ("Divinity: Original Sin 2", "rpg", "Des Sourciers s'echappent d'une colonie de Magisters.", 2017, "Larian Studios", "Swen Vincke", ""),
    ("Doom", "fps", "Un marine combat les demons sur Mars.", 1993, "id Software", "John Romero", ""),
    ("DOOM Eternal", "fps", "Le Doom Slayer poursuit son combat contre l'enfer.", 2020, "id Software", "Hugo Martin", ""),
    ("Doom II", "fps", "Une nouvelle invasion demoniaque menace la Terre.", 1994, "id Software", "John Romero", ""),
    ("Dragon Age: Origins", "rpg", "Un Garde des ombres unit le Ferelden contre le Fleau.", 2009, "BioWare", "Mike Laidlaw", ""),
    ("Duke Nukem 3D", "fps", "Un heros sarcastique repousse une invasion extraterrestre.", 1996, "3D Realms", "George Broussard", ""),
    ("Dune II", "rts", "Les maisons Atreides, Harkonnen et Ordos se disputent Arrakis.", 1992, "Westwood Studios", "Joe Bostic", ""),
    ("Dungeon Keeper", "gestion", "Le joueur gere un donjon maléfique et ses creatures.", 1997, "Bullfrog Productions", "Peter Molyneux", ""),
    ("Elden Ring", "rpg", "Un Sans-eclat parcourt l'Entre-terre pour devenir Seigneur d'Elden.", 2022, "FromSoftware", "Hidetaka Miyazaki", ""),
    ("Empire Earth", "rts", "Des nations evoluent de la Prehistoire a l'ere moderne.", 2001, "Stainless Steel Studios", "Rick Goodman", ""),
    ("Factorio", "gestion", "Un ingenieur automatise des chaines de production sur une planete hostile.", 2020, "Wube Software", "Michal Kovarik", ""),
    ("Fallout", "rpg", "Un habitant d'un abri part chercher une puce d'eau dans un monde post-apocalyptique.", 1997, "Black Isle Studios", "Tim Cain", ""),
    ("Fallout: New Vegas", "rpg", "Un coursier survit a une guerre de factions dans le Mojave.", 2010, "Obsidian Entertainment", "Josh Sawyer", ""),
    ("GoldenEye 007", "fps", "James Bond affronte un complot dans un jeu d'espionnage.", 1997, "Rare", "Martin Hollis", ""),
    ("Half-Life", "fps", "Gordon Freeman tente de survivre a un incident scientifique.", 1998, "Valve", "Gabe Newell", ""),
    ("Half-Life 2", "fps", "Gordon Freeman lutte contre l'occupation de la Terre.", 2004, "Valve", "Erik Johnson", ""),
    ("Halo: Combat Evolved", "fps", "Le Master Chief decouvre un anneau alien.", 2001, "Bungie", "Jason Jones", ""),
    ("Homeworld", "rts", "Une flotte spatiale cherche a retrouver sa planete natale.", 1999, "Relic Entertainment", "Alex Garden", ""),
    ("Left 4 Dead 2", "fps", "Quatre survivants cooperent face a une horde de zombies.", 2009, "Valve", "Mike Booth", ""),
    ("Mass Effect", "rpg", "Le commandant Shepard rassemble un equipage contre les Moissonneurs.", 2007, "BioWare", "Casey Hudson", ""),
    ("Overwatch", "fps", "Des heros aux roles varies combattent en equipe.", 2016, "Blizzard Entertainment", "Jeff Kaplan", ""),
    ("Persona 5", "rpg", "Des lyceens voleurs de coeurs combattent la corruption a Tokyo.", 2016, "Atlus", "Katsura Hashino", ""),
    ("Planescape: Torment", "rpg", "Un immortel cherche a comprendre son passe.", 1999, "Black Isle Studios", "Chris Avellone", ""),
    ("Planet Coaster", "gestion", "Un parc a theme est cree et gere.", 2016, "Frontier Developments", "David Braben", ""),
    ("Planet Zoo", "gestion", "Un parc zoologique est concu et entretenu.", 2019, "Frontier Developments", "Michael Brookes", ""),
    ("Portal 2", "fps", "Chell resout des enigmes avec un pistolet a portails.", 2011, "Valve", "Joshua Weier", ""),
    ("Prison Architect", "gestion", "Une prison est construite et administree.", 2015, "Introversion Software", "Chris Delay", ""),
    ("Quake", "fps", "Un combattant affronte les forces de Strogg.", 1996, "id Software", "John Romero", ""),
    ("Railroad Tycoon", "gestion", "Le joueur batit un empire ferroviaire au XIXe siecle.", 1990, "MicroProse", "Sid Meier", ""),
    ("RimWorld", "gestion", "Des colons survivent sur une planete lointaine.", 2018, "Ludeon Studios", "Tynan Sylvester", ""),
    ("RollerCoaster Tycoon", "gestion", "Un parc d'attractions est construit et exploite.", 1999, "Chris Sawyer Productions", "Chris Sawyer", ""),
    ("Rome: Total War", "rts", "Un general conquiert l'Empire romain avec strategie et batailles.", 2004, "Creative Assembly", "Mike Simpson", ""),
    ("SimCity", "gestion", "Le premier simulateur de construction et de gestion urbaine.", 1989, "Maxis", "Will Wright", ""),
    ("SimCity 2000", "gestion", "Le joueur construit et administre une ville.", 1993, "Maxis", "Will Wright", ""),
    ("Sins of a Solar Empire", "rts", "Des empires interstellaires se disputent la galaxie.", 2008, "Ironclad Games", "Blair Fraser", ""),
    ("Star Wars: Knights of the Old Republic", "rpg", "Un Jedi choisit son destin dans la galaxie.", 2003, "BioWare", "Casey Hudson", ""),
    ("StarCraft", "rts", "Terrans, Zergs et Protoss luttent pour le secteur Koprulu.", 1998, "Blizzard Entertainment", "Chris Metzen", ""),
    ("StarCraft II: Wings of Liberty", "rts", "Jim Raynor mene une rebellion contre le Dominion.", 2010, "Blizzard Entertainment", "Dustin Browder", ""),
    ("Supreme Commander", "rts", "Trois factions utilisent des armees futuristes a grande echelle.", 2007, "Gas Powered Games", "Chris Taylor", ""),
    ("Team Fortress 2", "fps", "Neuf classes de mercenaires s'opposent dans un style cartoon.", 2007, "Valve", "Robin Walker", ""),
    ("The Elder Scrolls III: Morrowind", "rpg", "Un elu explore l'ile volcanique de Vvardenfell.", 2002, "Bethesda Game Studios", "Todd Howard", ""),
    ("The Elder Scrolls V: Skyrim", "rpg", "Le Dovahkiin affronte les dragons de Bordeciel.", 2011, "Bethesda Game Studios", "Todd Howard", ""),
    ("The Sims", "gestion", "Le quotidien de personnages virtuels est organise par le joueur.", 2000, "Maxis", "Will Wright", ""),
    ("The Witcher 3: Wild Hunt", "rpg", "Geralt recherche Ciri dans un monde en guerre.", 2015, "CD Projekt RED", "Konrad Tomaszkiewicz", ""),
    ("Theme Hospital", "gestion", "Des hopitaux sont construits et geres avec humour.", 1997, "Bullfrog Productions", "Mark Webley", ""),
    ("Theme Park", "gestion", "Un parc d'attractions est construit et administre.", 1994, "Bullfrog Productions", "Peter Molyneux", ""),
    ("Titanfall 2", "fps", "Un pilote et son Titan combattent sur une planete en guerre.", 2016, "Respawn Entertainment", "Steve Fukuda", ""),
    ("Total Annihilation", "rts", "Deux factions robotiques se livrent une guerre totale.", 1997, "Cavedog Entertainment", "Chris Taylor", ""),
    ("Transport Tycoon", "gestion", "Un reseau de trains, bus, avions et bateaux est developpe.", 1994, "MicroProse", "Chris Sawyer", ""),
    ("Tropico", "gestion", "Un dictateur dirige une ile des Caraibes.", 2001, "PopTop Software", "Phil Steinmeyer", ""),
    ("Two Point Hospital", "gestion", "Un reseau d'hopitaux aux maladies insolites est gere.", 2018, "Two Point Studios", "Mark Webley", ""),
    ("Unreal Tournament", "fps", "Des combattants s'affrontent dans des arenes futuristes.", 1999, "Epic Games", "Cliff Bleszinski", ""),
    ("Vampire: The Masquerade - Bloodlines", "rpg", "Un jeune vampire decouvre la societe secrete de Los Angeles.", 2004, "Troika Games", "Leonard Boyarsky", ""),
    ("Warcraft II: Tides of Darkness", "rts", "Humains et orcs se livrent une guerre maritime.", 1995, "Blizzard Entertainment", "Bill Roper", ""),
    ("Warcraft III: Reign of Chaos", "rts", "Des heros conduisent leurs factions face a la Legion ardente.", 2002, "Blizzard Entertainment", "Rob Pardo", ""),
    ("Wolfenstein 3D", "fps", "Un soldat allie s'evade d'un chateau nazi.", 1992, "id Software", "John Romero", ""),
    ("Zoo Tycoon", "gestion", "Un zoo est amenage pour accueillir visiteurs et animaux.", 2001, "Blue Fang Games", "Eric Bowman", ""),
]

async def seed():
    await create_table()
    async with async_SessionLocal() as db:
        existants = set(await db.scalars(select(Items.titre)))
        for titre, categorie, description, annee, studio, directeur, image in CATALOGUE:
            if titre in existants:
                continue
            db.add(Items(
                titre=titre,
                categorie=categorie,
                description=description,
                annee=annee,
                studio=studio,
                directeur=directeur,
                image_url=image,
            ))
        await db.commit()
    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(seed())