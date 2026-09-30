import asyncio
from sqlalchemy import select
from .db.session import async_SessionLocal, create_table, engine
from .models.collection import Collection  
from .models.item import Items
from .models.user import Users 

CATALOGUE = [
    # ---------------- FPS ----------------
    ("Doom", "fps", "Un marine combat les demons sur Mars.", 1993, "id Software", "John Romero"),
    ("Doom II", "fps", "Une nouvelle invasion demoniaque menace la Terre.", 1994, "id Software", "John Romero"),
    ("Quake", "fps", "Un combattant affronte les forces de Strogg.", 1996, "id Software", "John Romero"),
    ("Half-Life", "fps", "Gordon Freeman tente de survivre a un incident scientifique.", 1998, "Valve", "Gabe Newell"),
    ("Counter-Strike", "fps", "Deux equipes s'affrontent dans des missions tactiques.", 2000, "Valve", "Minh Le"),
    ("Halo: Combat Evolved", "fps", "Le Master Chief decouvre un anneau alien.", 2001, "Bungie", "Jason Jones"),
    ("Call of Duty 4: Modern Warfare", "fps", "Des soldats menent des operations modernes.", 2007, "Infinity Ward", "Mackey McCandlish"),
    ("Borderlands 2", "fps", "Des chasseurs de l'Arche explorent Pandora.", 2012, "Gearbox Software", "Paul Sage"),
    ("Overwatch", "fps", "Des heros aux roles varies combattent en equipe.", 2016, "Blizzard Entertainment", "Jeff Kaplan"),
    ("DOOM Eternal", "fps", "Le Doom Slayer poursuit son combat contre l'enfer.", 2020, "id Software", "Hugo Martin"),
    ("Wolfenstein 3D", "fps", "Un soldat allie s'evade d'un chateau nazi.", 1992, "id Software", "John Romero"),
    ("Duke Nukem 3D", "fps", "Un heros sarcastique repousse une invasion extraterrestre.", 1996, "3D Realms", "George Broussard"),
    ("GoldenEye 007", "fps", "James Bond affronte un complot dans un jeu d'espionnage.", 1997, "Rare", "Martin Hollis"),
    ("Unreal Tournament", "fps", "Des combattants s'affrontent dans des arenes futuristes.", 1999, "Epic Games", "Cliff Bleszinski"),
    ("Half-Life 2", "fps", "Gordon Freeman lutte contre l'occupation de la Terre.", 2004, "Valve", "Erik Johnson"),
    ("Team Fortress 2", "fps", "Neuf classes de mercenaires s'opposent dans un style cartoon.", 2007, "Valve", "Robin Walker"),
    ("BioShock", "fps", "Un survivant explore la cite sous-marine de Rapture.", 2007, "2K Boston", "Ken Levine"),
    ("Left 4 Dead 2", "fps", "Quatre survivants cooperent face a une horde de zombies.", 2009, "Valve", "Mike Booth"),
    ("Portal 2", "fps", "Chell resout des enigmes avec un pistolet a portails.", 2011, "Valve", "Joshua Weier"),
    ("Titanfall 2", "fps", "Un pilote et son Titan combattent sur une planete en guerre.", 2016, "Respawn Entertainment", "Steve Fukuda"),
 
    # ---------------- RPG ----------------
    ("Baldur's Gate", "rpg", "Une aventure de role dans les Royaumes oublies.", 1998, "BioWare", "James Ohlen"),
    ("Planescape: Torment", "rpg", "Un immortel cherche a comprendre son passe.", 1999, "Black Isle Studios", "Chris Avellone"),
    ("Diablo II", "rpg", "Des heros affrontent les seigneurs des Enfers.", 2000, "Blizzard North", "David Brevik"),
    ("The Elder Scrolls III: Morrowind", "rpg", "Un elu explore l'ile volcanique de Vvardenfell.", 2002, "Bethesda Game Studios", "Todd Howard"),
    ("Star Wars: Knights of the Old Republic", "rpg", "Un Jedi choisit son destin dans la galaxie.", 2003, "BioWare", "Casey Hudson"),
    ("Mass Effect", "rpg", "Le commandant Shepard rassemble un equipage contre les Moissonneurs.", 2007, "BioWare", "Casey Hudson"),
    ("The Witcher 3: Wild Hunt", "rpg", "Geralt recherche Ciri dans un monde en guerre.", 2015, "CD Projekt RED", "Konrad Tomaszkiewicz"),
    ("Dark Souls III", "rpg", "Un Morteflamme explore un royaume en ruines.", 2016, "FromSoftware", "Hidetaka Miyazaki"),
    ("Divinity: Original Sin 2", "rpg", "Des Sourciers s'echappent d'une colonie de Magisters.", 2017, "Larian Studios", "Swen Vincke"),
    ("Elden Ring", "rpg", "Un Sans-eclat parcourt l'Entre-terre pour devenir Seigneur d'Elden.", 2022, "FromSoftware", "Hidetaka Miyazaki"),
    ("Fallout", "rpg", "Un habitant d'un abri part chercher une puce d'eau dans un monde post-apocalyptique.", 1997, "Black Isle Studios", "Tim Cain"),
    ("Baldur's Gate II: Shadows of Amn", "rpg", "Le heros de Baldur's Gate affronte le mage Jon Irenicus.", 2000, "BioWare", "James Ohlen"),
    ("Deus Ex", "rpg", "Un agent augmente enquete sur un complot mondial.", 2000, "Ion Storm", "Warren Spector"),
    ("Vampire: The Masquerade - Bloodlines", "rpg", "Un jeune vampire decouvre la societe secrete de Los Angeles.", 2004, "Troika Games", "Leonard Boyarsky"),
    ("Dragon Age: Origins", "rpg", "Un Garde des ombres unit le Ferelden contre le Fleau.", 2009, "BioWare", "Mike Laidlaw"),
    ("Fallout: New Vegas", "rpg", "Un coursier survit a une guerre de factions dans le Mojave.", 2010, "Obsidian Entertainment", "Josh Sawyer"),
    ("The Elder Scrolls V: Skyrim", "rpg", "Le Dovahkiin affronte les dragons de Bordeciel.", 2011, "Bethesda Game Studios", "Todd Howard"),
    ("Persona 5", "rpg", "Des lyceens voleurs de coeurs combattent la corruption a Tokyo.", 2016, "Atlus", "Katsura Hashino"),
    ("Disco Elysium", "rpg", "Un detective amnesique enquete dans la ville de Revachol.", 2019, "ZA/UM", "Robert Kurvitz"),
    ("Baldur's Gate 3", "rpg", "Des aventuriers infectes par un parasite mental cherchent un remede.", 2023, "Larian Studios", "Swen Vincke"),
 
    # ---------------- RTS ----------------
    ("Dune II", "rts", "Les maisons Atreides, Harkonnen et Ordos se disputent Arrakis.", 1992, "Westwood Studios", "Joe Bostic"),
    ("Warcraft II: Tides of Darkness", "rts", "Humains et orcs se livrent une guerre maritime.", 1995, "Blizzard Entertainment", "Bill Roper"),
    ("Command & Conquer: Red Alert", "rts", "Les Allies et les Sovietiques s'affrontent dans une histoire alternative.", 1996, "Westwood Studios", "Brett Sperry"),
    ("Age of Empires", "rts", "Des civilisations evoluent de l'Antiquite a l'age du fer.", 1997, "Ensemble Studios", "Rick Goodman"),
    ("StarCraft", "rts", "Terrans, Zergs et Protoss luttent pour le secteur Koprulu.", 1998, "Blizzard Entertainment", "Chris Metzen"),
    ("Warcraft III: Reign of Chaos", "rts", "Des heros conduisent leurs factions face a la Legion ardente.", 2002, "Blizzard Entertainment", "Rob Pardo"),
    ("Company of Heroes", "rts", "Des troupes alliees combattent en Europe pendant la Seconde Guerre mondiale.", 2006, "Relic Entertainment", "Quinn Duffy"),
    ("Supreme Commander", "rts", "Trois factions utilisent des armees futuristes a grande echelle.", 2007, "Gas Powered Games", "Chris Taylor"),
    ("StarCraft II: Wings of Liberty", "rts", "Jim Raynor mene une rebellion contre le Dominion.", 2010, "Blizzard Entertainment", "Dustin Browder"),
    ("Age of Empires IV", "rts", "Des civilisations historiques s'affrontent au Moyen Age.", 2021, "Relic Entertainment", "Adam Isgreen"),
    ("Command & Conquer", "rts", "Le GDI et le Nod se disputent le controle du Tiberium.", 1995, "Westwood Studios", "Brett Sperry"),
    ("Total Annihilation", "rts", "Deux factions robotiques se livrent une guerre totale.", 1997, "Cavedog Entertainment", "Chris Taylor"),
    ("Age of Empires II: The Age of Kings", "rts", "Des civilisations medievales se disputent la domination.", 1999, "Ensemble Studios", "Bruce Shelley"),
    ("Homeworld", "rts", "Une flotte spatiale cherche a retrouver sa planete natale.", 1999, "Relic Entertainment", "Alex Garden"),
    ("Empire Earth", "rts", "Des nations evoluent de la Prehistoire a l'ere moderne.", 2001, "Stainless Steel Studios", "Rick Goodman"),
    ("Age of Mythology", "rts", "Des dieux et des creatures mythiques s'invitent dans la guerre.", 2002, "Ensemble Studios", "Greg Street"),
    ("Command & Conquer: Generals", "rts", "Les Etats-Unis, la Chine et la GLA s'affrontent dans un conflit moderne.", 2003, "EA Pacific", "Mike Verdu"),
    ("Rome: Total War", "rts", "Un general conquiert l'Empire romain avec strategie et batailles.", 2004, "Creative Assembly", "Mike Simpson"),
    ("Sins of a Solar Empire", "rts", "Des empires interstellaires se disputent la galaxie.", 2008, "Ironclad Games", "Blair Fraser"),
    ("Company of Heroes 2", "rts", "Les Sovietiques affrontent la Wehrmacht sur le front de l'Est.", 2013, "Relic Entertainment", "Quinn Duffy"),
 
    # ---------------- Gestion ----------------
    ("SimCity 2000", "gestion", "Le joueur construit et administre une ville.", 1993, "Maxis", "Will Wright"),
    ("Theme Hospital", "gestion", "Des hopitaux sont construits et geres avec humour.", 1997, "Bullfrog Productions", "Mark Webley"),
    ("RollerCoaster Tycoon", "gestion", "Un parc d'attractions est construit et exploite.", 1999, "Chris Sawyer Productions", "Chris Sawyer"),
    ("The Sims", "gestion", "Le quotidien de personnages virtuels est organise par le joueur.", 2000, "Maxis", "Will Wright"),
    ("Zoo Tycoon", "gestion", "Un zoo est amenage pour accueillir visiteurs et animaux.", 2001, "Blue Fang Games", "Eric Bowman"),
    ("Prison Architect", "gestion", "Une prison est construite et administree.", 2015, "Introversion Software", "Chris Delay"),
    ("Cities: Skylines", "gestion", "Une metropole est planifiee et developpee.", 2015, "Colossal Order", "Mariina Hallikainen"),
    ("Planet Coaster", "gestion", "Un parc a theme est cree et gere.", 2016, "Frontier Developments", "David Braben"),
    ("Two Point Hospital", "gestion", "Un reseau d'hopitaux aux maladies insolites est gere.", 2018, "Two Point Studios", "Mark Webley"),
    ("Planet Zoo", "gestion", "Un parc zoologique est concu et entretenu.", 2019, "Frontier Developments", "Michael Brookes"),
    ("SimCity", "gestion", "Le premier simulateur de construction et de gestion urbaine.", 1989, "Maxis", "Will Wright"),
    ("Railroad Tycoon", "gestion", "Le joueur batit un empire ferroviaire au XIXe siecle.", 1990, "MicroProse", "Sid Meier"),
    ("Transport Tycoon", "gestion", "Un reseau de trains, bus, avions et bateaux est developpe.", 1994, "MicroProse", "Chris Sawyer"),
    ("Theme Park", "gestion", "Un parc d'attractions est construit et administre.", 1994, "Bullfrog Productions", "Peter Molyneux"),
    ("Dungeon Keeper", "gestion", "Le joueur gere un donjon maléfique et ses creatures.", 1997, "Bullfrog Productions", "Peter Molyneux"),
    ("Caesar III", "gestion", "Un gouverneur fait prosperer une cite de l'Empire romain.", 1998, "Impressions Games", "Simon Bradbury"),
    ("Anno 1602", "gestion", "Des colons developpent des iles et commercent en mer.", 1998, "Max Design", "Wilfried Reiter"),
    ("Tropico", "gestion", "Un dictateur dirige une ile des Caraibes.", 2001, "PopTop Software", "Phil Steinmeyer"),
    ("RimWorld", "gestion", "Des colons survivent sur une planete lointaine.", 2018, "Ludeon Studios", "Tynan Sylvester"),
    ("Factorio", "gestion", "Un ingenieur automatise des chaines de production sur une planete hostile.", 2020, "Wube Software", "Michal Kovarik"),
]

async def seed():
    await create_table()
    async with async_SessionLocal() as db:
        existants = set(await db.scalars(select(Items.titre)))
        for titre, categorie, description, annee, studio, directeur in CATALOGUE:
            if titre in existants:
                continue
            db.add(Items(
                titre=titre,
                categorie=categorie,
                description=description,
                annee=annee,
                studio="Inconnu",
                directeur="Inconnu",
                image_url="",
            ))
        await db.commit()
    await engine.dispose()

if __name__ == "__main__":
    asyncio.run(seed())