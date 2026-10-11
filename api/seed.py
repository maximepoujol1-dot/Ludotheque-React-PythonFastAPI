import asyncio
from sqlalchemy import select
from .db.session import async_SessionLocal, create_table, engine
from .models.collection import Collection
from .models.item import Items
from .models.user import Users

CATALOGUE = [
    ("Age of Empires", "rts", "Civilizations evolve from antiquity to the iron age.", 1997, "Ensemble Studios", "Rick Goodman", "https://static.wikia.nocookie.net/ageofempires/images/c/c4/Age_of_Empires_logo.png/revision/latest?cb=20150420140731&path-prefix=fr"),
    ("Age of Empires II: The Age of Kings", "rts", "Medieval civilizations compete for dominance.", 1999, "Ensemble Studios", "Bruce Shelley", "https://static.wikia.nocookie.net/ageofempires/images/c/cc/AoE2DE_logo.png/revision/latest/scale-to-width-down/1000?cb=20250227112959&path-prefix=fr"),
    ("Age of Empires IV", "rts", "Historical civilizations clash in the Middle Ages.", 2021, "Relic Entertainment", "Adam Isgreen", "https://static.wikia.nocookie.net/ageofempires/images/1/12/Logo-age4-vert-1.png/revision/latest?cb=20170821203233"),
    ("Age of Mythology", "rts", "Gods and mythical creatures join the warfare.", 2002, "Ensemble Studios", "Greg Street", "https://static.wikia.nocookie.net/ageofempires/images/e/e0/Logo_AoMR.png/revision/latest/scale-to-width-down/1000?cb=20240609182923"),
    ("Anno 1602", "gestion", "Colonists develop islands and trade overseas.", 1998, "Max Design", "Wilfried Reiter", "https://thumb.wikimedia.org/wikipedia/fr/thumb/2/23/Anno_1602_Logo.png/250px-Anno_1602_Logo.png?utm_source=fr.wikipedia.org&utm_campaign=parser&utm_content=thumbnail"),
    ("Baldur's Gate", "rpg", "A role-playing adventure in the Forgotten Realms.", 1998, "BioWare", "James Ohlen", "https://fr.wikipedia.org/wiki/Fichier:Baldur's_Gate_Logo.png"),
    ("Baldur's Gate II: Shadows of Amn", "rpg", "The hero of Baldur's Gate confronts the mage Jon Irenicus.", 2000, "BioWare", "James Ohlen", "https://thumb.wikimedia.org/wikipedia/fr/thumb/6/62/Baldur%27s_Gate_II_Shadows_of_Amn_Logo.png/250px-Baldur%27s_Gate_II_Shadows_of_Amn_Logo.png?utm_source=fr.wikipedia.org&utm_campaign=parser&utm_content=thumbnail"),
    ("Baldur's Gate 3", "rpg", "Adventurers infected by a mind parasite seek a cure.", 2023, "Larian Studios", "Swen Vincke", "https://thumb.wikimedia.org/wikipedia/fr/thumb/d/dc/Baldur%27s_Gate_III_Logo.png/250px-Baldur%27s_Gate_III_Logo.png?utm_source=fr.wikipedia.org&utm_campaign=parser&utm_content=thumbnail"),
    ("BioShock", "fps", "A survivor explores the underwater city of Rapture.", 2007, "2K Boston", "Ken Levine", ""),
    ("Borderlands 2", "fps", "Vault Hunters explore Pandora.", 2012, "Gearbox Software", "Paul Sage", ""),
    ("Caesar III", "gestion", "A governor prospers a city of the Roman Empire.", 1998, "Impressions Games", "Simon Bradbury", ""),
    ("Call of Duty 4: Modern Warfare", "fps", "Soldiers lead modern operations.", 2007, "Infinity Ward", "Mackey McCandlish", ""),
    ("Cities: Skylines", "gestion", "A metropolis is planned and developed.", 2015, "Colossal Order", "Mariina Hallikainen", ""),
    ("Command & Conquer", "rts", "GDI and Nod fight for control of Tiberium.", 1995, "Westwood Studios", "Brett Sperry", ""),
    ("Command & Conquer: Generals", "rts", "The USA, China, and the GLA clash in a modern conflict.", 2003, "EA Pacific", "Mike Verdu", ""),
    ("Command & Conquer: Red Alert", "rts", "Allies and Soviets fight in an alternate history.", 1996, "Westwood Studios", "Brett Sperry", ""),
    ("Company of Heroes", "rts", "Allied troops fight in Europe during World War II.", 2006, "Relic Entertainment", "Quinn Duffy", ""),
    ("Company of Heroes 2", "rts", "Soviets confront the Wehrmacht on the Eastern Front.", 2013, "Relic Entertainment", "Quinn Duffy", ""),
    ("Counter-Strike", "fps", "Two teams compete in tactical missions.", 2000, "Valve", "Minh Le", ""),
    ("Dark Souls III", "rpg", "An Ashen One explores a ruined kingdom.", 2016, "FromSoftware", "Hidetaka Miyazaki", ""),
    ("Deus Ex", "rpg", "An augmented agent investigates a global conspiracy.", 2000, "Ion Storm", "Warren Spector", ""),
    ("Diablo II", "rpg", "Heroes face the lords of the Burning Hells.", 2000, "Blizzard North", "David Brevik", ""),
    ("Disco Elysium", "rpg", "An amnesiac detective investigates in the city of Revachol.", 2019, "ZA/UM", "Robert Kurvitz", ""),
    ("Divinity: Original Sin 2", "rpg", "Sourcerers escape from a Magister colony.", 2017, "Larian Studios", "Swen Vincke", ""),
    ("Doom", "fps", "A marine fights demons on Mars.", 1993, "id Software", "John Romero", ""),
    ("DOOM Eternal", "fps", "The Doom Slayer continues his fight against hell.", 2020, "id Software", "Hugo Martin", ""),
    ("Doom II", "fps", "A new demonic invasion threatens Earth.", 1994, "id Software", "John Romero", ""),
    ("Dragon Age: Origins", "rpg", "A Grey Warden unites Ferelden against the Blight.", 2009, "BioWare", "Mike Laidlaw", ""),
    ("Duke Nukem 3D", "fps", "A sarcastic hero repels an alien invasion.", 1996, "3D Realms", "George Broussard", ""),
    ("Dune II", "rts", "Houses Atreides, Harkonnen, and Ordos fight for Arrakis.", 1992, "Westwood Studios", "Joe Bostic", ""),
    ("Dungeon Keeper", "gestion", "The player manages an evil dungeon and its creatures.", 1997, "Bullfrog Productions", "Peter Molyneux", ""),
    ("Elden Ring", "rpg", "A Tarnished travels the Lands Between to become Elden Lord.", 2022, "FromSoftware", "Hidetaka Miyazaki", ""),
    ("Empire Earth", "rts", "Nations evolve from prehistory to the modern era.", 2001, "Stainless Steel Studios", "Rick Goodman", ""),
    ("Factorio", "gestion", "An engineer automates production lines on a hostile planet.", 2020, "Wube Software", "Michal Kovarik", ""),
    ("Fallout", "rpg", "A vault dweller searches for a water chip in a post-apocalyptic world.", 1997, "Black Isle Studios", "Tim Cain", ""),
    ("Fallout: New Vegas", "rpg", "A courier survives a faction war in the Mojave.", 2010, "Obsidian Entertainment", "Josh Sawyer", ""),
    ("GoldenEye 007", "fps", "James Bond faces a conspiracy in a spy game.", 1997, "Rare", "Martin Hollis", ""),
    ("Half-Life", "fps", "Gordon Freeman tries to survive a scientific incident.", 1998, "Valve", "Gabe Newell", ""),
    ("Half-Life 2", "fps", "Gordon Freeman fights against the occupation of Earth.", 2004, "Valve", "Erik Johnson", ""),
    ("Halo: Combat Evolved", "fps", "Master Chief discovers an alien ring.", 2001, "Bungie", "Jason Jones", ""),
    ("Homeworld", "rts", "A space fleet seeks to find its home planet.", 1999, "Relic Entertainment", "Alex Garden", ""),
    ("Left 4 Dead 2", "fps", "Four survivors cooperate against a horde of zombies.", 2009, "Valve", "Mike Booth", ""),
    ("Mass Effect", "rpg", "Commander Shepard gathers a crew against the Reapers.", 2007, "BioWare", "Casey Hudson", ""),
    ("Overwatch", "fps", "Heroes with varied roles fight in teams.", 2016, "Blizzard Entertainment", "Jeff Kaplan", ""),
    ("Persona 5", "rpg", "High school phantom thieves fight corruption in Tokyo.", 2016, "Atlus", "Katsura Hashino", ""),
    ("Planescape: Torment", "rpg", "An immortal seeks to understand his past.", 1999, "Black Isle Studios", "Chris Avellone", ""),
    ("Planet Coaster", "gestion", "A theme park is created and managed.", 2016, "Frontier Developments", "David Braben", ""),
    ("Planet Zoo", "gestion", "A zoological park is designed and maintained.", 2019, "Frontier Developments", "Michael Brookes", ""),
    ("Portal 2", "fps", "Chell solves puzzles with a portal gun.", 2011, "Valve", "Joshua Weier", ""),
    ("Prison Architect", "gestion", "A prison is built and administered.", 2015, "Introversion Software", "Chris Delay", ""),
    ("Quake", "fps", "A fighter faces the forces of Strogg.", 1996, "id Software", "John Romero", ""),
    ("Railroad Tycoon", "gestion", "The player builds a railroad empire in the 19th century.", 1990, "MicroProse", "Sid Meier", ""),
    ("RimWorld", "gestion", "Colonists survive on a distant planet.", 2018, "Ludeon Studios", "Tynan Sylvester", ""),
    ("RollerCoaster Tycoon", "gestion", "An amusement park is built and operated.", 1999, "Chris Sawyer Productions", "Chris Sawyer", ""),
    ("Rome: Total War", "rts", "A general conquers the Roman Empire with strategy and battles.", 2004, "Creative Assembly", "Mike Simpson", ""),
    ("SimCity", "gestion", "The first urban construction and management simulator.", 1989, "Maxis", "Will Wright", ""),
    ("SimCity 2000", "gestion", "The player builds and administers a city.", 1993, "Maxis", "Will Wright", ""),
    ("Sins of a Solar Empire", "rts", "Interstellar empires compete for the galaxy.", 2008, "Ironclad Games", "Blair Fraser", ""),
    ("Star Wars: Knights of the Old Republic", "rpg", "A Jedi chooses their destiny in the galaxy.", 2003, "BioWare", "Casey Hudson", ""),
    ("StarCraft", "rts", "Terrans, Zergs, and Protoss fight for the Koprulu sector.", 1998, "Blizzard Entertainment", "Chris Metzen", ""),
    ("StarCraft II: Wings of Liberty", "rts", "Jim Raynor leads a rebellion against the Dominion.", 2010, "Blizzard Entertainment", "Dustin Browder", ""),
    ("Supreme Commander", "rts", "Three factions use large-scale futuristic armies.", 2007, "Gas Powered Games", "Chris Taylor", ""),
    ("Team Fortress 2", "fps", "Nine mercenary classes oppose each other in a cartoon style.", 2007, "Valve", "Robin Walker", ""),
    ("The Elder Scrolls III: Morrowind", "rpg", "A chosen one explores the volcanic island of Vvardenfell.", 2002, "Bethesda Game Studios", "Todd Howard", ""),
    ("The Elder Scrolls V: Skyrim", "rpg", "The Dragonborn confronts the dragons of Skyrim.", 2011, "Bethesda Game Studios", "Todd Howard", ""),
    ("The Sims", "gestion", "The daily life of virtual characters is organized by the player.", 2000, "Maxis", "Will Wright", ""),
    ("The Witcher 3: Wild Hunt", "rpg", "Geralt searches for Ciri in a war-torn world.", 2015, "CD Projekt RED", "Konrad Tomaszkiewicz", ""),
    ("Theme Hospital", "gestion", "Hospitals are built and managed with humor.", 1997, "Bullfrog Productions", "Mark Webley", ""),
    ("Theme Park", "gestion", "An amusement park is built and administered.", 1994, "Bullfrog Productions", "Peter Molyneux", ""),
    ("Titanfall 2", "fps", "A pilot and their Titan fight on a war-torn planet.", 2016, "Respawn Entertainment", "Steve Fukuda", ""),
    ("Total Annihilation", "rts", "Two robotic factions wage total war.", 1997, "Cavedog Entertainment", "Chris Taylor", ""),
    ("Transport Tycoon", "gestion", "A network of trains, buses, planes, and boats is developed.", 1994, "MicroProse", "Chris Sawyer", ""),
    ("Tropico", "gestion", "A dictator rules a Caribbean island.", 2001, "PopTop Software", "Phil Steinmeyer", ""),
    ("Two Point Hospital", "gestion", "A network of hospitals with unusual illnesses is managed.", 2018, "Two Point Studios", "Mark Webley", ""),
    ("Unreal Tournament", "fps", "Fighters face off in futuristic arenas.", 1999, "Epic Games", "Cliff Bleszinski", ""),
    ("Vampire: The Masquerade - Bloodlines", "rpg", "A young vampire discovers the secret society of Los Angeles.", 2004, "Troika Games", "Leonard Boyarsky", ""),
    ("Warcraft II: Tides of Darkness", "rts", "Humans and orcs wage a maritime war.", 1995, "Blizzard Entertainment", "Bill Roper", ""),
    ("Warcraft III: Reign of Chaos", "rts", "Heroes lead their factions against the Burning Legion.", 2002, "Blizzard Entertainment", "Rob Pardo", ""),
    ("Wolfenstein 3D", "fps", "An allied soldier escapes a Nazi castle.", 1992, "id Software", "John Romero", ""),
    ("Zoo Tycoon", "gestion", "A zoo is arranged to welcome visitors and animals.", 2001, "Blue Fang Games", "Eric Bowman", ""),
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
