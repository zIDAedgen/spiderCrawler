'''
PY[^PY]{0, 10}
'''
import re




#1.Location : The 'plus' house has class = _3fbupa, this will be a label to check whether a house is a plus one
#2.status
#3.introduction
#4.Amenities: _iq8x9is 2 to 15
from bs4 import BeautifulSoup





path = './htmls/4.html'
txt = './urls.txt'
htmlfile = open(path, 'r', encoding='utf-8')
htmlhandle = htmlfile.read()
urls = []

def get_urls_plus():
    soup = BeautifulSoup(htmlhandle, 'lxml')
    l = soup.find_all(class_ = '_e296pg')
    print(len(l))
    print(l)
    for i in range(1, len(l)):
        print(l[i])
        print('id')
        #print(l[i]['href'].split('/')[-1])
        print("img source")
        #print('img' + l[i].img['src'])
        print()
def get_urls():
    soup = BeautifulSoup(htmlhandle, 'lxml')

    l = soup.find_all(class_ = '_16lonkd')
    print(len(l))
    print(l)
    for i in range(len(l)):
        print('id')
        print(l[i]['href'].split('/')[-1])
        print("img source")
        print('img' + l[i].img['src'])
        print()
'''
def write_into_file():
    with open(txt, 'w') as f:
        for url in urls:
            f.write("%s\n" % url)
'''



get_urls_plus()
nameString = "Claude Howell(s)Chester JohnDinah MarthaMaurice GladstoneIna EleanorTracy MarnerArno EdmundMichaelia GillHermosa SinclairBeacher PaulAndrea BrowneBowen RalphDouglas YuleLouis JuddMyra ToursNicholas BirdClark BloomfieldJoshua LondonUla LandonDerrick LeightonJonas WebsterCara WillNicola HazlittEartha LucyBlithe CoffeyRae MacPhersonLarry Aled(k)Herman JerryEmma PriestleyRudolf GarciaArchibald KingsleyGustave II.Leif GallacherByron MaryClyde EisenhowerJerry ArabellaCaroline IvanGemma JessieGeorgia RhysErin ArchibaldRaymond JuliaMurphy FordArlene FlynnErnest CharlesBeatrice HarrodLynnJean CarterLisa WhitmanJessie RoseEdith WarrenPenelope AlbertJeremy WillardGeorge GroteElvira HarrimanKaren MelvilleZona WhitMerle Wyld(e)Tyler DaltonJesse DoyleHugh GrayAfra OscarLesley Mat(h)ildaVincent BethuneRose LowellAlma CharleyStan Lindberg(h)Bonnie DuBoisMiriam GeoffreyDonna YoungDarcy NancyZero LawsonMichell AddisonEden RussellNewman NahumHunter GilbertNovia BobbyMarvin Sara(h)Peter JonathanPandora NorthIra IV.Webb MargeryAgatha TonyDeniseLou WhittierAugustine RomeoHiram MaloryLewis DeQuinceyVicky LouiseDonahue HamletAlexander ElsieLiz CarlRod KeppelCatherine DunbarHugo LindsayHubery BernardAthena JennyRex ConradIda GosseWill AttleeAbraham RogerSophia LeacockReg SheridanMerlin MarkAbbott PeterNelly FingerMatthew WellsCandice HaydnJoyce BrownSigrid AlickVerne EzekielLilith III.Page WhiteheadGeraldine HuxleyBess WilliamCleveland LucasYetta GreenDiana BrightGrover YeatesBurnell BecherDevin MooreGale SimonGuy MarcellusFord MichelsonBing JackRosemary CecilliaDick StevensonAnastasia FitzGeraldCamille PulitzerTom SanderGilbert BarrieDave PrittDoreen NicholasOscar ElectraIsaac ClareKim EmilyEllis PriceWarner TimothyHazel GeorgeVeromcaLance Wyclif(fe)Uriah CroftSean BloorCaesar RobesonYork AdamsGloria BelleJared OnionsBorg BenjaminAntonio LynchMarlon RoyPayne PullanReginald HaggaiDarlene NoelGavin WildeEdmund SonmerfieldAbigail Jenkin(s)Otto Nichol(s)Clarence BlumeNeil BellocVito AndersonRock TurnerKerwin TolandAdairJune RaphaelChad MasefieldMorton NickBert DrydenPrudence CarolineWanda AugustineDarren WilsonShirley RolandQuincy BensonEileen QuillerHilda BarnardLaura BrookCherry BeckSusan WatNathan WaltonSpring BroadBart IrvingMoses LuciusFreda ClaraBradley BeerbohmColbertIsabel DoraLen FastAmos Burne-JonesSharon MorseAgnes EipsteinArmand MarloweVivien FeltonZachary FunkJacqueline SassoonZoeBarry JoanVictoria ToynbeeClement MortonXaviera EugeneJulie MoultonParker TrumanEverley MarshallTyrone BobMay TrollpoeThera PerkinAlvis ChristianaEnid LouisaHenry RuthTroy HarperMolly FrancesOlivia PansyMavis NortonTruman GeordieClara ConanCash JoeLorraine CissieFaitheMarsh HansenKitty BettyGill LewisTodd PaterJamie AnneSandra KelvinCharles ChristWerner MosesWebster MoreWade HodgeTobey DewarMiles CarnegieBurton KatteNatividad ArnoldMaggie BertramVerna WagnerStephanie StilwellFanny MartinVictor HuttCecil ToutAlexia HubbardHamiltion NewmanMiranda HarveyHilary JacksonBrook AleranderArmstrong WodehousMabel KatrineBard HooverBertram LizzieEden TaylorMatt FinnZebulon ZechariahMartha KelsenMonica WallisFay EllisRachel RaglanWalter MollLyndon SharpLeona ShakespeareSamantha SaulLynn CoverdaleFerdinand SaxtonDominic HewlettIrma DeliaMadge GreshamChristine BloomerChristopher LongmanRuth EuphemiaRodney RosaBennett EdenColin DanVeronica StracheyPolly KiplingEdwina JeremyDempsey JeremiahChapman DarwinAdam WarnerCarl MatthewQuinn PitmanViolet MalanBrian LattimoreDuke ThorndikeWendell IsaiahAngelo JohnsonErica ReadeSolomon WesleyWinni CareyHarry SteinbeckRegan PiersAnnabelle KittyMadeline CamillaDolores McCarthyMarguerite GunterRobert DillonRonald SophiaSteven BakerAntonia StephenLennon HabakkukBarton MeredithWinfred GuyGeoffrey ClementSampson ClaphamSteward JoshuaCynthia DupontHarvey WalterMaxwell FosterAsa RaleignMichael SamLucien YerkesDwight PollyPete ByronEmily LewLevi TheresaRuby LaurieSarah BessRobin BowmanJoan JulietAtwood WildAnn SmedleyWinifred WollastonOdelette TedJill DuncanBeck IsabelCrystal WebbOsborn HowardKyle LuciaLeonard Gard(i)nerAbel SpenserJohn DickeyMonroe PollittWilbur CromwellNoel ScrippsAntony PeggyEdwiin NoraJeff SteelePaula HaroldCoral AntoinetteHarley BuckAaron FergusonIan TempleBarret WalkleyToby HoratioQuintion CharlotteOliver BradleyMoore ConstanceBarnett DeweyMeredith AchesonDaniel MicahChristian HenryWendy JimArcher IsaacEve HoustonJoseph PepysMamie CrichtonEnoch KeynesDean VanLena JohnsonJerome ChristopherFlora TobiasColby FerdinandLouise JasperBelle CurmeEarl GilesStanley MikeRoy LeopoldMax WilcoxKelly LancelotApril Alsop(p)Hardy WinifredBlanche SwinburneEvelyn CarpenterKatherine ChurchMartina BerkeleyBishop TylerTiffany VeblenRandolph MondEdward WilhelminaZara EdithBenedict DavidPamela MaggieRiva PhilemonOphelia RobbinsWayne PopeFranklin ChristianBrandon BrookeAdonis ReynoldsAstrid EdwardKay ThompsonCornell NehemiahElla VincentValentina RobVivian JudithLinda Wyat(t)Bill RuskSpencer HaywoodAries FrederickBartholomew Humphr(e)yJuliet ConnieMarico MonroeChasel RichardBroderick LouisDunn GrahamElvis SilasKelly AntoniaCharlotte LambertDorothy HertyEric ShawRenee JoshJocelyn IngersollBridget StellaTiffany ElizabethKeith CarllyleFlorence JonsonNelson O'CaseyMoira BabbittBeryl BuckleRita ScottNora AldingtonYvette HartDora PeacockMarina ThackerayChrist SmithArthur DonneJenny NathanieiRegina CommonsWinston HenleyRalap MayJoanne NellyJo WalkerHaley CroftsEdison MorleyRenata MacAdamMaxine LincolnBoyd RamsdenNathaniel HughesWillie MacaulayMyron EllenHerbert RichardsonFelix WattWright EvansAmy HarteSetlla GracePhyllis BenHulda Kell(e)yBernard BillyEvangeline BaldwinGustave CraigieElma GibbonKerr AnnSalome ThodoreHobart EugenSandy GardenJudy KentLetitia AustinGeneAnsel DierserMark HudsonDaisy ShelleyStacey ChristieMona ChildBeau MariaOctavia NeedhamQuintina BenedictBen BarneyAlan MiddletonGregary TommySheila LyndHale JosephQueena SusannaJoyce CooperSebastiane ArmstrongSam AbrahamAugus MotleyPatricia BrunoHedda JoyceTheodore MegLeila BunyanBerton RichardsLawrence PatrickBaldwin BertieOlga MalachiMartin LylyAudrey BarrettJulian LenaElmer ClemensJosephine AdelaFitch EllaBaron JoelJudith BennettWallis MaudHoney BrowningLindsay JeffersonCliff SallyAurora KatharineOdelia RicardoIvan GrantTed LeeTab JohnnyNorton GallupIrene PegMaria SandyBaird BartholomewTracy GabrielTina Hopkin(s)Carol Abbot(t)Lauren JulianaJulius BessieAlvin RosalindIris WheelerRory LukeJack BillEsther AlfredBruno SpencerMichelle StephensSebastian HalifaxAdela Johnston(e)James HoraceJanice JuliusTruda BrayMagee ForsterDana AdelaideConstance FelixLaurel TwainLillian ZimmermanMarcia EdgeworthJustin BessemerPorter CumberlandStanford GoldBernice ZangwillRoberta WalshDeborah HoyleSusie EvaLambert KathleenBoris HansomBetsy ChurchillElsie ParkerTeresa FoxGlenn ServiceHorace TrevelyanElsa ThomasCorey MansfieldJay BauerNina SpenderArlen VictorPage RooseveltJane UlyssesAmanda I.Cheryl JenningsBurgess BurkeGabriel YonngKristin GissingKen SainsburyAndre DullesGriselda ChristyFrank CongreveAlva GuntherLeo ZephaniahLydia HenriettaEugene StrongGordon MaxwellZora NoahBooth RossettiYves ArthurAvery GaskellBasil OrlandoDylanRon MalthusDana CarrollVirgil SapirHarriet TobyMalcolm RaymondMag ReedEudora KennedyCuritis HughJim GusAbner GalsworthyOlive FannyLionel GreyEvan JeanGail DaniellNicole GoldsmithMarcus HuntingtonRyan SwiftChanning MorganElijah RockefellerMary MaltzDuncan BachHeloise OccamPhoenix ButlerRupert NelsonJulia HopeMarian BlackPearl LockeVera MarjoryUpton MarcusGriffith JonesSandy SaroyanJo BoyleMontague EvePatrick WindsorJonathan GodwinNydia SailsburyDale Ackerman(n)Ward SamsonBob BoswellFrederica JamesBenjamin RebeccaElroy LongfellowMike BertNoah TitusBlake FredXenia JeamesKevin MontgomeryVenus HearstChloe SpringhallBelinda CollinsNorman TateSusanna EliotXanthe LawrenceBruce TracyEd BeaufortElizabeth BlakeRoderick AgnesVita BrewsterSibyl WardElliot AustenIngemar MichaelHyman SusanPerry BryanTheobald CottonCalvin AldridgeOwen MargaretOrville FrancisSimona CarmenZenobia RuskinArvin ChildeAllen EddieTim MorrisonSara OliverDoris AlyGenevieve LyttonEgbert CraneDonald FieldingSabrina JudsonJacob HemingwayMignon AdamBertha AnnaJoy GracieFrances KelloggBevis VirginiaAlbert FrankJason MiltonDon Den(n)isHogan ErnestPag ColcloughHarold LilyDeirdre ChaucerPaul AmeliaTony HoseaGodfery StoneHelen WheatleyElva ChapmanOgden HobbesNatalie HousmanMurray EdiePenny WoolleyWilliam VaughanMilo ElinorAngela JouleAugust EmmaAlva CarrieBblythe GregoryHannah EffieOtis HawthorneTabitha O'NeilCyril AnthonyKing BartlettCecilia TerryGary Nico(l)Alice ZachariasCornelius O'ConnorBeverly PearsonJennifer ChamberlainAmelia OwenNancy TomAndy HouseNat CroninDavid CockerKama CowperLes SnowClare SoutheyBarbara RobinsonThomas NixonValentine PhilipMuriel GranthamMandy JaneOswald AdolphSamuel PoeJessica EstherSid MarionMaureen HumePrimo MacDonaldKennedy BenthamDaphne MauriceVirginia NoyesIngrid HalCathy DefoeBlair BaconBurke HugginsViola SamuelBernie BowenCarr"
nameSets = nameString.split(" ")
print(len(nameSets))
