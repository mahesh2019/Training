
from neo4j.v1 import GraphDatabase
uri             = "bolt://localhost:7687"

userName        = "neo4j"

password        = "mahesh@1994"

graphDB_Driver  = GraphDatabase.driver(uri, auth=(userName, password))

query="""create (TheMatrix:Movie {title:'The Matrix', released:1999, tagline:'Welcome to the Real World'})
 (Keanu:Person {name:'Keanu Reeves', born:1964})
 (Carrie:Person {name:'Carrie-Anne Moss', born:1967})
 (Laurence:Person {name:'Laurence Fishburne', born:1961})
 (Hugo:Person {name:'Hugo Weaving', born:1960})
 (LillyW:Person {name:'Lilly Wachowski', born:1967})
 (LanaW:Person {name:'Lana Wachowski', born:1965})
 (JoelS:Person {name:'Joel Silver', born:1952})

  (Keanu)-[:ACTED_IN {roles:['Neo']}]->(TheMatrix),
  (Carrie)-[:ACTED_IN {roles:['Trinity']}]->(TheMatrix),
  (Laurence)-[:ACTED_IN {roles:['Morpheus']}]->(TheMatrix),
  (Hugo)-[:ACTED_IN {roles:['Agent Smith']}]->(TheMatrix),
  (LillyW)-[:DIRECTED]->(TheMatrix),
  (LanaW)-[:DIRECTED]->(TheMatrix),
  (JoelS)-[:PRODUCED]->(TheMatrix)

 (Emil:Person {name:"Emil Eifrem", born:1978})
 (Emil)-[:ACTED_IN {roles:["Emil"]}]->(TheMatrix)

 (TheMatrixReloaded:Movie {title:'The Matrix Reloaded', released:2003, tagline:'Free your mind'})

  (Keanu)-[:ACTED_IN {roles:['Neo']}]->(TheMatrixReloaded),
  (Carrie)-[:ACTED_IN {roles:['Trinity']}]->(TheMatrixReloaded),
  (Laurence)-[:ACTED_IN {roles:['Morpheus']}]->(TheMatrixReloaded),
  (Hugo)-[:ACTED_IN {roles:['Agent Smith']}]->(TheMatrixReloaded),
  (LillyW)-[:DIRECTED]->(TheMatrixReloaded),
  (LanaW)-[:DIRECTED]->(TheMatrixReloaded),
  (JoelS)-[:PRODUCED]->(TheMatrixReloaded)

 (TheMatrixRevolutions:Movie {title:'The Matrix Revolutions', released:2003, tagline:'Everything that has a beginning has an end'})

  (Keanu)-[:ACTED_IN {roles:['Neo']}]->(TheMatrixRevolutions),
  (Carrie)-[:ACTED_IN {roles:['Trinity']}]->(TheMatrixRevolutions),
  (Laurence)-[:ACTED_IN {roles:['Morpheus']}]->(TheMatrixRevolutions),
  (Hugo)-[:ACTED_IN {roles:['Agent Smith']}]->(TheMatrixRevolutions),
  (LillyW)-[:DIRECTED]->(TheMatrixRevolutions),
  (LanaW)-[:DIRECTED]->(TheMatrixRevolutions),
  (JoelS)-[:PRODUCED]->(TheMatrixRevolutions)

 (TheDevilsAdvocate:Movie {title:"The Devil's Advocate", released:1997, tagline:'Evil has its winning ways'})
 (Charlize:Person {name:'Charlize Theron', born:1975})
 (Al:Person {name:'Al Pacino', born:1940})
 (Taylor:Person {name:'Taylor Hackford', born:1944})

  (Keanu)-[:ACTED_IN {roles:['Kevin Lomax']}]->(TheDevilsAdvocate),
  (Charlize)-[:ACTED_IN {roles:['Mary Ann Lomax']}]->(TheDevilsAdvocate),
  (Al)-[:ACTED_IN {roles:['John Milton']}]->(TheDevilsAdvocate),
  (Taylor)-[:DIRECTED]->(TheDevilsAdvocate)

 (AFewGoodMen:Movie {title:"A Few Good Men", released:1992, tagline:"In the heart of the nation's capital, in a courthouse of the U.S. government, one man will stop at nothing to keep his honor, and one will stop at nothing to find the truth."})
 (TomC:Person {name:'Tom Cruise', born:1962})
 (JackN:Person {name:'Jack Nicholson', born:1937})
 (DemiM:Person {name:'Demi Moore', born:1962})
 (KevinB:Person {name:'Kevin Bacon', born:1958})
 (KieferS:Person {name:'Kiefer Sutherland', born:1966})
 (NoahW:Person {name:'Noah Wyle', born:1971})
 (CubaG:Person {name:'Cuba Gooding Jr.', born:1968})
 (KevinP:Person {name:'Kevin Pollak', born:1957})
 (JTW:Person {name:'J.T. Walsh', born:1943})
 (JamesM:Person {name:'James Marshall', born:1967})
 (ChristopherG:Person {name:'Christopher Guest', born:1948})
 (RobR:Person {name:'Rob Reiner', born:1947})
 (AaronS:Person {name:'Aaron Sorkin', born:1961})

  (TomC)-[:ACTED_IN {roles:['Lt. Daniel Kaffee']}]->(AFewGoodMen),
  (JackN)-[:ACTED_IN {roles:['Col. Nathan R. Jessup']}]->(AFewGoodMen),
  (DemiM)-[:ACTED_IN {roles:['Lt. Cdr. JoAnne Galloway']}]->(AFewGoodMen),
  (KevinB)-[:ACTED_IN {roles:['Capt. Jack Ross']}]->(AFewGoodMen),
  (KieferS)-[:ACTED_IN {roles:['Lt. Jonathan Kendrick']}]->(AFewGoodMen),
  (NoahW)-[:ACTED_IN {roles:['Cpl. Jeffrey Barnes']}]->(AFewGoodMen),
  (CubaG)-[:ACTED_IN {roles:['Cpl. Carl Hammaker']}]->(AFewGoodMen),
  (KevinP)-[:ACTED_IN {roles:['Lt. Sam Weinberg']}]->(AFewGoodMen),
  (JTW)-[:ACTED_IN {roles:['Lt. Col. Matthew Andrew Markinson']}]->(AFewGoodMen),
  (JamesM)-[:ACTED_IN {roles:['Pfc. Louden Downey']}]->(AFewGoodMen),
  (ChristopherG)-[:ACTED_IN {roles:['Dr. Stone']}]->(AFewGoodMen),
  (AaronS)-[:ACTED_IN {roles:['Man in Bar']}]->(AFewGoodMen),
  (RobR)-[:DIRECTED]->(AFewGoodMen),
  (AaronS)-[:WROTE]->(AFewGoodMen)

 (TopGun:Movie {title:"Top Gun", released:1986, tagline:'I feel the need, the need for speed.'})
 (KellyM:Person {name:'Kelly McGillis', born:1957})
 (ValK:Person {name:'Val Kilmer', born:1959})
 (AnthonyE:Person {name:'Anthony Edwards', born:1962})
 (TomS:Person {name:'Tom Skerritt', born:1933})
 (MegR:Person {name:'Meg Ryan', born:1961})
 (TonyS:Person {name:'Tony Scott', born:1944})
 (JimC:Person {name:'Jim Cash', born:1941})

  (TomC)-[:ACTED_IN {roles:['Maverick']}]->(TopGun),
  (KellyM)-[:ACTED_IN {roles:['Charlie']}]->(TopGun),
  (ValK)-[:ACTED_IN {roles:['Iceman']}]->(TopGun),
  (AnthonyE)-[:ACTED_IN {roles:['Goose']}]->(TopGun),
  (TomS)-[:ACTED_IN {roles:['Viper']}]->(TopGun),
  (MegR)-[:ACTED_IN {roles:['Carole']}]->(TopGun),
  (TonyS)-[:DIRECTED]->(TopGun),
  (JimC)-[:WROTE]->(TopGun)

 (JerryMaguire:Movie {title:'Jerry Maguire', released:2000, tagline:'The rest of his life begins now.'})
 (ReneeZ:Person {name:'Renee Zellweger', born:1969})
 (KellyP:Person {name:'Kelly Preston', born:1962})
 (JerryO:Person {name:"Jerry O'Connell", born:1974})
 (JayM:Person {name:'Jay Mohr', born:1970})
 (BonnieH:Person {name:'Bonnie Hunt', born:1961})
 (ReginaK:Person {name:'Regina King', born:1971})
 (JonathanL:Person {name:'Jonathan Lipnicki', born:1996})
 (CameronC:Person {name:'Cameron Crowe', born:1957})

  (TomC)-[:ACTED_IN {roles:['Jerry Maguire']}]->(JerryMaguire),
  (CubaG)-[:ACTED_IN {roles:['Rod Tidwell']}]->(JerryMaguire),
  (ReneeZ)-[:ACTED_IN {roles:['Dorothy Boyd']}]->(JerryMaguire),
  (KellyP)-[:ACTED_IN {roles:['Avery Bishop']}]->(JerryMaguire),
  (JerryO)-[:ACTED_IN {roles:['Frank Cushman']}]->(JerryMaguire),
  (JayM)-[:ACTED_IN {roles:['Bob Sugar']}]->(JerryMaguire),
  (BonnieH)-[:ACTED_IN {roles:['Laurel Boyd']}]->(JerryMaguire),
  (ReginaK)-[:ACTED_IN {roles:['Marcee Tidwell']}]->(JerryMaguire),
  (JonathanL)-[:ACTED_IN {roles:['Ray Boyd']}]->(JerryMaguire),
  (CameronC)-[:DIRECTED]->(JerryMaguire),
  (CameronC)-[:PRODUCED]->(JerryMaguire),
  (CameronC)-[:WROTE]->(JerryMaguire)

 (StandByMe:Movie {title:"Stand By Me", released:1986, tagline:"For some, it's the last real taste of innocence, and the first real taste of life. But for everyone, it's the time that memories are made of."})
 (RiverP:Person {name:'River Phoenix', born:1970})
 (CoreyF:Person {name:'Corey Feldman', born:1971})
 (WilW:Person {name:'Wil Wheaton', born:1972})
 (JohnC:Person {name:'John Cusack', born:1966})
 (MarshallB:Person {name:'Marshall Bell', born:1942})

  (WilW)-[:ACTED_IN {roles:['Gordie Lachance']}]->(StandByMe),
  (RiverP)-[:ACTED_IN {roles:['Chris Chambers']}]->(StandByMe),
  (JerryO)-[:ACTED_IN {roles:['Vern Tessio']}]->(StandByMe),
  (CoreyF)-[:ACTED_IN {roles:['Teddy Duchamp']}]->(StandByMe),
  (JohnC)-[:ACTED_IN {roles:['Denny Lachance']}]->(StandByMe),
  (KieferS)-[:ACTED_IN {roles:['Ace Merrill']}]->(StandByMe),
  (MarshallB)-[:ACTED_IN {roles:['Mr. Lachance']}]->(StandByMe),
  (RobR)-[:DIRECTED]->(StandByMe)

 (AsGoodAsItGets:Movie {title:'As Good as It Gets', released:1997, tagline:'A comedy from the heart that goes for the throat.'})
 (HelenH:Person {name:'Helen Hunt', born:1963})
 (GregK:Person {name:'Greg Kinnear', born:1963})
 (JamesB:Person {name:'James L. Brooks', born:1940})

  (JackN)-[:ACTED_IN {roles:['Melvin Udall']}]->(AsGoodAsItGets),
  (HelenH)-[:ACTED_IN {roles:['Carol Connelly']}]->(AsGoodAsItGets),
  (GregK)-[:ACTED_IN {roles:['Simon Bishop']}]->(AsGoodAsItGets),
  (CubaG)-[:ACTED_IN {roles:['Frank Sachs']}]->(AsGoodAsItGets),
  (JamesB)-[:DIRECTED]->(AsGoodAsItGets)

 (WhatDreamsMayCome:Movie {title:'What Dreams May Come', released:1998, tagline:'After life there is more. The end is just the beginning.'})
 (AnnabellaS:Person {name:'Annabella Sciorra', born:1960})
 (MaxS:Person {name:'Max von Sydow', born:1929})
 (WernerH:Person {name:'Werner Herzog', born:1942})
 (Robin:Person {name:'Robin Williams', born:1951})
 (VincentW:Person {name:'Vincent Ward', born:1956})

  (Robin)-[:ACTED_IN {roles:['Chris Nielsen']}]->(WhatDreamsMayCome),
  (CubaG)-[:ACTED_IN {roles:['Albert Lewis']}]->(WhatDreamsMayCome),
  (AnnabellaS)-[:ACTED_IN {roles:['Annie Collins-Nielsen']}]->(WhatDreamsMayCome),
  (MaxS)-[:ACTED_IN {roles:['The Tracker']}]->(WhatDreamsMayCome),
  (WernerH)-[:ACTED_IN {roles:['The Face']}]->(WhatDreamsMayCome),
  (VincentW)-[:DIRECTED]->(WhatDreamsMayCome)

 (SnowFallingonCedars:Movie {title:'Snow Falling on Cedars', released:1999, tagline:'First loves last. Forever.'})
 (EthanH:Person {name:'Ethan Hawke', born:1970})
 (RickY:Person {name:'Rick Yune', born:1971})
 (JamesC:Person {name:'James Cromwell', born:1940})
 (ScottH:Person {name:'Scott Hicks', born:1953})

  (EthanH)-[:ACTED_IN {roles:['Ishmael Chambers']}]->(SnowFallingonCedars),
  (RickY)-[:ACTED_IN {roles:['Kazuo Miyamoto']}]->(SnowFallingonCedars),
  (MaxS)-[:ACTED_IN {roles:['Nels Gudmundsson']}]->(SnowFallingonCedars),
  (JamesC)-[:ACTED_IN {roles:['Judge Fielding']}]->(SnowFallingonCedars),
  (ScottH)-[:DIRECTED]->(SnowFallingonCedars)

 (YouveGotMail:Movie {title:"You've Got Mail", released:1998, tagline:'At odds in life... in love on-line.'})
 (ParkerP:Person {name:'Parker Posey', born:1968})
 (DaveC:Person {name:'Dave Chappelle', born:1973})
 (SteveZ:Person {name:'Steve Zahn', born:1967})
 (TomH:Person {name:'Tom Hanks', born:1956})
 (NoraE:Person {name:'Nora Ephron', born:1941})

  (TomH)-[:ACTED_IN {roles:['Joe Fox']}]->(YouveGotMail),
  (MegR)-[:ACTED_IN {roles:['Kathleen Kelly']}]->(YouveGotMail),
  (GregK)-[:ACTED_IN {roles:['Frank Navasky']}]->(YouveGotMail),
  (ParkerP)-[:ACTED_IN {roles:['Patricia Eden']}]->(YouveGotMail),
  (DaveC)-[:ACTED_IN {roles:['Kevin Jackson']}]->(YouveGotMail),
  (SteveZ)-[:ACTED_IN {roles:['George Pappas']}]->(YouveGotMail),
  (NoraE)-[:DIRECTED]->(YouveGotMail)

 (SleeplessInSeattle:Movie {title:'Sleepless in Seattle', released:1993, tagline:'What if someone you never met, someone you never saw, someone you never knew was the only someone for you?'})
 (RitaW:Person {name:'Rita Wilson', born:1956})
 (BillPull:Person {name:'Bill Pullman', born:1953})
 (VictorG:Person {name:'Victor Garber', born:1949})
 (RosieO:Person {name:"Rosie O'Donnell", born:1962})

  (TomH)-[:ACTED_IN {roles:['Sam Baldwin']}]->(SleeplessInSeattle),
  (MegR)-[:ACTED_IN {roles:['Annie Reed']}]->(SleeplessInSeattle),
  (RitaW)-[:ACTED_IN {roles:['Suzy']}]->(SleeplessInSeattle),
  (BillPull)-[:ACTED_IN {roles:['Walter']}]->(SleeplessInSeattle),
  (VictorG)-[:ACTED_IN {roles:['Greg']}]->(SleeplessInSeattle),
  (RosieO)-[:ACTED_IN {roles:['Becky']}]->(SleeplessInSeattle),
  (NoraE)-[:DIRECTED]->(SleeplessInSeattle)

 (JoeVersustheVolcano:Movie {title:'Joe Versus the Volcano', released:1990, tagline:'A story of love, lava and burning desire.'})
 (JohnS:Person {name:'John Patrick Stanley', born:1950})
 (Nathan:Person {name:'Nathan Lane', born:1956})

  (TomH)-[:ACTED_IN {roles:['Joe Banks']}]->(JoeVersustheVolcano),
  (MegR)-[:ACTED_IN {roles:['DeDe', 'Angelica Graynamore', 'Patricia Graynamore']}]->(JoeVersustheVolcano),
  (Nathan)-[:ACTED_IN {roles:['Baw']}]->(JoeVersustheVolcano),
  (JohnS)-[:DIRECTED]->(JoeVersustheVolcano)

 (WhenHarryMetSally:Movie {title:'When Harry Met Sally', released:1998, tagline:'At odds in life... in love on-line.'})
 (BillyC:Person {name:'Billy Crystal', born:1948})
 (CarrieF:Person {name:'Carrie Fisher', born:1956})
 (BrunoK:Person {name:'Bruno Kirby', born:1949})

  (BillyC)-[:ACTED_IN {roles:['Harry Burns']}]->(WhenHarryMetSally),
  (MegR)-[:ACTED_IN {roles:['Sally Albright']}]->(WhenHarryMetSally),
  (CarrieF)-[:ACTED_IN {roles:['Marie']}]->(WhenHarryMetSally),
  (BrunoK)-[:ACTED_IN {roles:['Jess']}]->(WhenHarryMetSally),
  (RobR)-[:DIRECTED]->(WhenHarryMetSally),
  (RobR)-[:PRODUCED]->(WhenHarryMetSally),
  (NoraE)-[:PRODUCED]->(WhenHarryMetSally),
  (NoraE)-[:WROTE]->(WhenHarryMetSally)

 (ThatThingYouDo:Movie {title:'That Thing You Do', released:1996, tagline:'In every life there comes a time when that thing you dream becomes that thing you do'})
 (LivT:Person {name:'Liv Tyler', born:1977})

  (TomH)-[:ACTED_IN {roles:['Mr. White']}]->(ThatThingYouDo),
  (LivT)-[:ACTED_IN {roles:['Faye Dolan']}]->(ThatThingYouDo),
  (Charlize)-[:ACTED_IN {roles:['Tina']}]->(ThatThingYouDo),
  (TomH)-[:DIRECTED]->(ThatThingYouDo)

 (TheReplacements:Movie {title:'The Replacements', released:2000, tagline:'Pain heals, Chicks dig scars... Glory lasts forever'})
 (Brooke:Person {name:'Brooke Langton', born:1970})
 (Gene:Person {name:'Gene Hackman', born:1930})
 (Orlando:Person {name:'Orlando Jones', born:1968})
 (Howard:Person {name:'Howard Deutch', born:1950})

  (Keanu)-[:ACTED_IN {roles:['Shane Falco']}]->(TheReplacements),
  (Brooke)-[:ACTED_IN {roles:['Annabelle Farrell']}]->(TheReplacements),
  (Gene)-[:ACTED_IN {roles:['Jimmy McGinty']}]->(TheReplacements),
  (Orlando)-[:ACTED_IN {roles:['Clifford Franklin']}]->(TheReplacements),
  (Howard)-[:DIRECTED]->(TheReplacements)

 (RescueDawn:Movie {title:'RescueDawn', released:2006, tagline:"Based on the extraordinary true story of one man's fight for freedom"})
 (ChristianB:Person {name:'Christian Bale', born:1974})
 (ZachG:Person {name:'Zach Grenier', born:1954})

  (MarshallB)-[:ACTED_IN {roles:['Admiral']}]->(RescueDawn),
  (ChristianB)-[:ACTED_IN {roles:['Dieter Dengler']}]->(RescueDawn),
  (ZachG)-[:ACTED_IN {roles:['Squad Leader']}]->(RescueDawn),
  (SteveZ)-[:ACTED_IN {roles:['Duane']}]->(RescueDawn),
  (WernerH)-[:DIRECTED]->(RescueDawn)

 (TheBirdcage:Movie {title:'The Birdcage', released:1996, tagline:'Come as you are'})
 (MikeN:Person {name:'Mike Nichols', born:1931})

  (Robin)-[:ACTED_IN {roles:['Armand Goldman']}]->(TheBirdcage),
  (Nathan)-[:ACTED_IN {roles:['Albert Goldman']}]->(TheBirdcage),
  (Gene)-[:ACTED_IN {roles:['Sen. Kevin Keeley']}]->(TheBirdcage),
  (MikeN)-[:DIRECTED]->(TheBirdcage)

 (Unforgiven:Movie {title:'Unforgiven', released:1992, tagline:"It's a hell of a thing, killing a man"})
 (RichardH:Person {name:'Richard Harris', born:1930})
 (ClintE:Person {name:'Clint Eastwood', born:1930})

  (RichardH)-[:ACTED_IN {roles:['English Bob']}]->(Unforgiven),
  (ClintE)-[:ACTED_IN {roles:['Bill Munny']}]->(Unforgiven),
  (Gene)-[:ACTED_IN {roles:['Little Bill Daggett']}]->(Unforgiven),
  (ClintE)-[:DIRECTED]->(Unforgiven)

 (JohnnyMnemonic:Movie {title:'Johnny Mnemonic', released:1995, tagline:'The hottest data on earth. In the coolest head in town'})
 (Takeshi:Person {name:'Takeshi Kitano', born:1947})
 (Dina:Person {name:'Dina Meyer', born:1968})
 (IceT:Person {name:'Ice-T', born:1958})
 (RobertL:Person {name:'Robert Longo', born:1953})

  (Keanu)-[:ACTED_IN {roles:['Johnny Mnemonic']}]->(JohnnyMnemonic),
  (Takeshi)-[:ACTED_IN {roles:['Takahashi']}]->(JohnnyMnemonic),
  (Dina)-[:ACTED_IN {roles:['Jane']}]->(JohnnyMnemonic),
  (IceT)-[:ACTED_IN {roles:['J-Bone']}]->(JohnnyMnemonic),
  (RobertL)-[:DIRECTED]->(JohnnyMnemonic)

 (CloudAtlas:Movie {title:'Cloud Atlas', released:2012, tagline:'Everything is connected'})
 (HalleB:Person {name:'Halle Berry', born:1966})
 (JimB:Person {name:'Jim Broadbent', born:1949})
 (TomT:Person {name:'Tom Tykwer', born:1965})
 (DavidMitchell:Person {name:'David Mitchell', born:1969})
 (StefanArndt:Person {name:'Stefan Arndt', born:1961})

  (TomH)-[:ACTED_IN {roles:['Zachry', 'Dr. Henry Goose', 'Isaac Sachs', 'Dermot Hoggins']}]->(CloudAtlas),
  (Hugo)-[:ACTED_IN {roles:['Bill Smoke', 'Haskell Moore', 'Tadeusz Kesselring', 'Nurse Noakes', 'Boardman Mephi', 'Old Georgie']}]->(CloudAtlas),
  (HalleB)-[:ACTED_IN {roles:['Luisa Rey', 'Jocasta Ayrs', 'Ovid', 'Meronym']}]->(CloudAtlas),
  (JimB)-[:ACTED_IN {roles:['Vyvyan Ayrs', 'Captain Molyneux', 'Timothy Cavendish']}]->(CloudAtlas),
  (TomT)-[:DIRECTED]->(CloudAtlas),
  (LillyW)-[:DIRECTED]->(CloudAtlas),
  (LanaW)-[:DIRECTED]->(CloudAtlas),
  (DavidMitchell)-[:WROTE]->(CloudAtlas),
  (StefanArndt)-[:PRODUCED]->(CloudAtlas)

 (TheDaVinciCode:Movie {title:'The Da Vinci Code', released:2006, tagline:'Break The Codes'})
 (IanM:Person {name:'Ian McKellen', born:1939})
 (AudreyT:Person {name:'Audrey Tautou', born:1976})
 (PaulB:Person {name:'Paul Bettany', born:1971})
 (RonH:Person {name:'Ron Howard', born:1954})

  (TomH)-[:ACTED_IN {roles:['Dr. Robert Langdon']}]->(TheDaVinciCode),
  (IanM)-[:ACTED_IN {roles:['Sir Leight Teabing']}]->(TheDaVinciCode),
  (AudreyT)-[:ACTED_IN {roles:['Sophie Neveu']}]->(TheDaVinciCode),
  (PaulB)-[:ACTED_IN {roles:['Silas']}]->(TheDaVinciCode),
  (RonH)-[:DIRECTED]->(TheDaVinciCode)

 (VforVendetta:Movie {title:'V for Vendetta', released:2006, tagline:'Freedom! Forever!'})
 (NatalieP:Person {name:'Natalie Portman', born:1981})
 (StephenR:Person {name:'Stephen Rea', born:1946})
 (JohnH:Person {name:'John Hurt', born:1940})
 (BenM:Person {name: 'Ben Miles', born:1967})

  (Hugo)-[:ACTED_IN {roles:['V']}]->(VforVendetta),
  (NatalieP)-[:ACTED_IN {roles:['Evey Hammond']}]->(VforVendetta),
  (StephenR)-[:ACTED_IN {roles:['Eric Finch']}]->(VforVendetta),
  (JohnH)-[:ACTED_IN {roles:['High Chancellor Adam Sutler']}]->(VforVendetta),
  (BenM)-[:ACTED_IN {roles:['Dascomb']}]->(VforVendetta),
  (JamesM)-[:DIRECTED]->(VforVendetta),
  (LillyW)-[:PRODUCED]->(VforVendetta),
  (LanaW)-[:PRODUCED]->(VforVendetta),
  (JoelS)-[:PRODUCED]->(VforVendetta),
  (LillyW)-[:WROTE]->(VforVendetta),
  (LanaW)-[:WROTE]->(VforVendetta)

 (SpeedRacer:Movie {title:'Speed Racer', released:2008, tagline:'Speed has no limits'})
 (EmileH:Person {name:'Emile Hirsch', born:1985})
 (JohnG:Person {name:'John Goodman', born:1960})
 (SusanS:Person {name:'Susan Sarandon', born:1946})
 (MatthewF:Person {name:'Matthew Fox', born:1966})
 (ChristinaR:Person {name:'Christina Ricci', born:1980})
 (Rain:Person {name:'Rain', born:1982})

  (EmileH)-[:ACTED_IN {roles:['Speed Racer']}]->(SpeedRacer),
  (JohnG)-[:ACTED_IN {roles:['Pops']}]->(SpeedRacer),
  (SusanS)-[:ACTED_IN {roles:['Mom']}]->(SpeedRacer),
  (MatthewF)-[:ACTED_IN {roles:['Racer X']}]->(SpeedRacer),
  (ChristinaR)-[:ACTED_IN {roles:['Trixie']}]->(SpeedRacer),
  (Rain)-[:ACTED_IN {roles:['Taejo Togokahn']}]->(SpeedRacer),
  (BenM)-[:ACTED_IN {roles:['Cass Jones']}]->(SpeedRacer),
  (LillyW)-[:DIRECTED]->(SpeedRacer),
  (LanaW)-[:DIRECTED]->(SpeedRacer),
  (LillyW)-[:WROTE]->(SpeedRacer),
  (LanaW)-[:WROTE]->(SpeedRacer),
  (JoelS)-[:PRODUCED]->(SpeedRacer)

 (NinjaAssassin:Movie {title:'Ninja Assassin', released:2009, tagline:'Prepare to enter a secret world of assassins'})
 (NaomieH:Person {name:'Naomie Harris'})

  (Rain)-[:ACTED_IN {roles:['Raizo']}]->(NinjaAssassin),
  (NaomieH)-[:ACTED_IN {roles:['Mika Coretti']}]->(NinjaAssassin),
  (RickY)-[:ACTED_IN {roles:['Takeshi']}]->(NinjaAssassin),
  (BenM)-[:ACTED_IN {roles:['Ryan Maslow']}]->(NinjaAssassin),
  (JamesM)-[:DIRECTED]->(NinjaAssassin),
  (LillyW)-[:PRODUCED]->(NinjaAssassin),
  (LanaW)-[:PRODUCED]->(NinjaAssassin),
  (JoelS)-[:PRODUCED]->(NinjaAssassin)

 (TheGreenMile:Movie {title:'The Green Mile', released:1999, tagline:"Walk a mile you'll never forget."})
 (MichaelD:Person {name:'Michael Clarke Duncan', born:1957})
 (DavidM:Person {name:'David Morse', born:1953})
 (SamR:Person {name:'Sam Rockwell', born:1968})
 (GaryS:Person {name:'Gary Sinise', born:1955})
 (PatriciaC:Person {name:'Patricia Clarkson', born:1959})
 (FrankD:Person {name:'Frank Darabont', born:1959})

  (TomH)-[:ACTED_IN {roles:['Paul Edgecomb']}]->(TheGreenMile),
  (MichaelD)-[:ACTED_IN {roles:['John Coffey']}]->(TheGreenMile),
  (DavidM)-[:ACTED_IN {roles:['Brutus "Brutal" Howell']}]->(TheGreenMile),
  (BonnieH)-[:ACTED_IN {roles:['Jan Edgecomb']}]->(TheGreenMile),
  (JamesC)-[:ACTED_IN {roles:['Warden Hal Moores']}]->(TheGreenMile),
  (SamR)-[:ACTED_IN {roles:['"Wild Bill" Wharton']}]->(TheGreenMile),
  (GaryS)-[:ACTED_IN {roles:['Burt Hammersmith']}]->(TheGreenMile),
  (PatriciaC)-[:ACTED_IN {roles:['Melinda Moores']}]->(TheGreenMile),
  (FrankD)-[:DIRECTED]->(TheGreenMile)

 (FrostNixon:Movie {title:'Frost/Nixon', released:2008, tagline:'400 million people were waiting for the truth.'})
 (FrankL:Person {name:'Frank Langella', born:1938})
 (MichaelS:Person {name:'Michael Sheen', born:1969})
 (OliverP:Person {name:'Oliver Platt', born:1960})

  (FrankL)-[:ACTED_IN {roles:['Richard Nixon']}]->(FrostNixon),
  (MichaelS)-[:ACTED_IN {roles:['David Frost']}]->(FrostNixon),
  (KevinB)-[:ACTED_IN {roles:['Jack Brennan']}]->(FrostNixon),
  (OliverP)-[:ACTED_IN {roles:['Bob Zelnick']}]->(FrostNixon),
  (SamR)-[:ACTED_IN {roles:['James Reston, Jr.']}]->(FrostNixon),
  (RonH)-[:DIRECTED]->(FrostNixon)

 (Hoffa:Movie {title:'Hoffa', released:1992, tagline:"He didn't want law. He wanted justice."})
 (DannyD:Person {name:'Danny DeVito', born:1944})
 (JohnR:Person {name:'John C. Reilly', born:1965})

  (JackN)-[:ACTED_IN {roles:['Hoffa']}]->(Hoffa),
  (DannyD)-[:ACTED_IN {roles:['Robert "Bobby" Ciaro']}]->(Hoffa),
  (JTW)-[:ACTED_IN {roles:['Frank Fitzsimmons']}]->(Hoffa),
  (JohnR)-[:ACTED_IN {roles:['Peter "Pete" Connelly']}]->(Hoffa),
  (DannyD)-[:DIRECTED]->(Hoffa)

 (Apollo13:Movie {title:'Apollo 13', released:1995, tagline:'Houston, we have a problem.'})
 (EdH:Person {name:'Ed Harris', born:1950})
 (BillPax:Person {name:'Bill Paxton', born:1955})

  (TomH)-[:ACTED_IN {roles:['Jim Lovell']}]->(Apollo13),
  (KevinB)-[:ACTED_IN {roles:['Jack Swigert']}]->(Apollo13),
  (EdH)-[:ACTED_IN {roles:['Gene Kranz']}]->(Apollo13),
  (BillPax)-[:ACTED_IN {roles:['Fred Haise']}]->(Apollo13),
  (GaryS)-[:ACTED_IN {roles:['Ken Mattingly']}]->(Apollo13),
  (RonH)-[:DIRECTED]->(Apollo13)

 (Twister:Movie {title:'Twister', released:1996, tagline:"Don't Breathe. Don't Look Back."})
 (PhilipH:Person {name:'Philip Seymour Hoffman', born:1967})
 (JanB:Person {name:'Jan de Bont', born:1943})

  (BillPax)-[:ACTED_IN {roles:['Bill Harding']}]->(Twister),
  (HelenH)-[:ACTED_IN {roles:['Dr. Jo Harding']}]->(Twister),
  (ZachG)-[:ACTED_IN {roles:['Eddie']}]->(Twister),
  (PhilipH)-[:ACTED_IN {roles:['Dustin "Dusty" Davis']}]->(Twister),
  (JanB)-[:DIRECTED]->(Twister)

 (CastAway:Movie {title:'Cast Away', released:2000, tagline:'At the edge of the world, his journey begins.'})
 (RobertZ:Person {name:'Robert Zemeckis', born:1951})

  (TomH)-[:ACTED_IN {roles:['Chuck Noland']}]->(CastAway),
  (HelenH)-[:ACTED_IN {roles:['Kelly Frears']}]->(CastAway),
  (RobertZ)-[:DIRECTED]->(CastAway)

 (OneFlewOvertheCuckoosNest:Movie {title:"One Flew Over the Cuckoo's Nest", released:1975, tagline:"If he's crazy, what does that make you?"})
 (MilosF:Person {name:'Milos Forman', born:1932})

  (JackN)-[:ACTED_IN {roles:['Randle McMurphy']}]->(OneFlewOvertheCuckoosNest),
  (DannyD)-[:ACTED_IN {roles:['Martini']}]->(OneFlewOvertheCuckoosNest),
  (MilosF)-[:DIRECTED]->(OneFlewOvertheCuckoosNest)

 (SomethingsGottaGive:Movie {title:"Something's Gotta Give", released:2003})
 (DianeK:Person {name:'Diane Keaton', born:1946})
 (NancyM:Person {name:'Nancy Meyers', born:1949})

  (JackN)-[:ACTED_IN {roles:['Harry Sanborn']}]->(SomethingsGottaGive),
  (DianeK)-[:ACTED_IN {roles:['Erica Barry']}]->(SomethingsGottaGive),
  (Keanu)-[:ACTED_IN {roles:['Julian Mercer']}]->(SomethingsGottaGive),
  (NancyM)-[:DIRECTED]->(SomethingsGottaGive),
  (NancyM)-[:PRODUCED]->(SomethingsGottaGive),
  (NancyM)-[:WROTE]->(SomethingsGottaGive)

 (BicentennialMan:Movie {title:'Bicentennial Man', released:1999, tagline:"One robot's 200 year journey to become an ordinary man."})
 (ChrisC:Person {name:'Chris Columbus', born:1958})

  (Robin)-[:ACTED_IN {roles:['Andrew Marin']}]->(BicentennialMan),
  (OliverP)-[:ACTED_IN {roles:['Rupert Burns']}]->(BicentennialMan),
  (ChrisC)-[:DIRECTED]->(BicentennialMan)

 (CharlieWilsonsWar:Movie {title:"Charlie Wilson's War", released:2007, tagline:"A stiff drink. A little mascara. A lot of nerve. Who said they couldn't bring down the Soviet empire."})
 (JuliaR:Person {name:'Julia Roberts', born:1967})

  (TomH)-[:ACTED_IN {roles:['Rep. Charlie Wilson']}]->(CharlieWilsonsWar),
  (JuliaR)-[:ACTED_IN {roles:['Joanne Herring']}]->(CharlieWilsonsWar),
  (PhilipH)-[:ACTED_IN {roles:['Gust Avrakotos']}]->(CharlieWilsonsWar),
  (MikeN)-[:DIRECTED]->(CharlieWilsonsWar)

 (ThePolarExpress:Movie {title:'The Polar Express', released:2004, tagline:'This Holiday Season… Believe'})

  (TomH)-[:ACTED_IN {roles:['Hero Boy', 'Father', 'Conductor', 'Hobo', 'Scrooge', 'Santa Claus']}]->(ThePolarExpress),
  (RobertZ)-[:DIRECTED]->(ThePolarExpress)

 (ALeagueofTheirOwn:Movie {title:'A League of Their Own', released:1992, tagline:'Once in a lifetime you get a chance to do something different.'})
 (Madonna:Person {name:'Madonna', born:1954})
 (GeenaD:Person {name:'Geena Davis', born:1956})
 (LoriP:Person {name:'Lori Petty', born:1963})
 (PennyM:Person {name:'Penny Marshall', born:1943})

  (TomH)-[:ACTED_IN {roles:['Jimmy Dugan']}]->(ALeagueofTheirOwn),
  (GeenaD)-[:ACTED_IN {roles:['Dottie Hinson']}]->(ALeagueofTheirOwn),
  (LoriP)-[:ACTED_IN {roles:['Kit Keller']}]->(ALeagueofTheirOwn),
  (RosieO)-[:ACTED_IN {roles:['Doris Murphy']}]->(ALeagueofTheirOwn),
  (Madonna)-[:ACTED_IN {roles:['"All the Way" Mae Mordabito']}]->(ALeagueofTheirOwn),
  (BillPax)-[:ACTED_IN {roles:['Bob Hinson']}]->(ALeagueofTheirOwn),
  (PennyM)-[:DIRECTED]->(ALeagueofTheirOwn)

 (PaulBlythe:Person {name:'Paul Blythe'})
 (AngelaScope:Person {name:'Angela Scope'})
 (JessicaThompson:Person {name:'Jessica Thompson'})
 (JamesThompson:Person {name:'James Thompson'})


  (JamesThompson)-[:FOLLOWS]->(JessicaThompson),
  (AngelaScope)-[:FOLLOWS]->(JessicaThompson),
  (PaulBlythe)-[:FOLLOWS]->(AngelaScope)


  (JessicaThompson)-[:REVIEWED {summary:'An amazing journey', rating:95}]->(CloudAtlas),
  (JessicaThompson)-[:REVIEWED {summary:'Silly, but fun', rating:65}]->(TheReplacements),
  (JamesThompson)-[:REVIEWED {summary:'The coolest football movie ever', rating:100}]->(TheReplacements),
  (AngelaScope)-[:REVIEWED {summary:'Pretty funny at times', rating:62}]->(TheReplacements),
  (JessicaThompson)-[:REVIEWED {summary:'Dark, but compelling', rating:85}]->(Unforgiven),
  (JessicaThompson)-[:REVIEWED {summary:"Slapstick redeemed only by the Robin Williams and Gene Hackman's stellar performances", rating:45}]->(TheBirdcage),
  (JessicaThompson)-[:REVIEWED {summary:'A solid romp', rating:68}]->(TheDaVinciCode),
  (JamesThompson)-[:REVIEWED {summary:'Fun, but a little far fetched', rating:65}]->(TheDaVinciCode),
  (JessicaThompson)-[:REVIEWED {summary:'You had me at Jerry', rating:92}]->(JerryMaguire)

WITH TomH as a
MATCH (a)-[:ACTED_IN]->(m)<-[:DIRECTED]-(d) RETURN a,m,d LIMIT 10
""" 
with graphDB_Driver.session() as graphDB_Session:
    graphDB_Session.run(query)
