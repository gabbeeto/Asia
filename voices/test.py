import wave
from piper import PiperVoice

texts = [
    """Welcome to our exhibition about Asia!""",
    """Indian subcontinent — mainly India itself.""",
    """Why Europeans came:
    Europeans don't have spices so bland food
    spread christianity""",
    """“There's a reason why there are too many Asian restaurants all over the world.”
    (There's a few Europeans restaurant though)""",
    """The ottoman empire controlled Asian trading""",
    """European colonization in India began with the Portuguese.""",
    """Several empires set up trading posts, but only the British, French, and Portuguese survived into the 20th century.""",
    """The British East India Company, initially a trading entity, established small coastal forts.""",
    """At that time, the powerful Mughal Empire ruled most of India, controlling 27% of the world economy—equal to all of China or Western Europe combined. Direct European conquest was impossible because the Mughals had strong shipbuilding, textile, and trade networks.""",
    """However, in the early 18th century, Invasions from Persia and Afghanistan caused external strains on the state. At the same time, the regions within the Empire began demanding more autonomy. England happened to be withing the region it was first breaking away""",
    """The East India Company saw the fall of the Mughal Empire as an opportunity. As regions fought succession wars, the British supported one claimant with superior artillery and warships. Once their side won, they placed a company official in charge of that state's treasury, controlling tax collection and government spending, with a large portion sent to London shareholders.""",
    """If rulers disagreed, the British threatened bombardment. Through these "unequal treaties," they gained control of Bengal, Bihar, and Orissa's finances by 1765.""",
    """British government officials were also company shareholders, so they passed legislation to strengthen the company.""",
    """They invested taxes into hiring Indian mercenaries and training Indian soldiers, expanding their conquests.""",
    """Some land was directly ruled, while princely states remained under Indian princes who paid tribute. (Those states pay the company so they still rule in those lands btw...)""",
    """Over time, taxes increased, land was confiscated, and regions became opium farms for trade with China.""",
    """The British destroyed Indian industries (steel, shipbuilding, textiles) by taxing Indian goods heavily while exempting British imports, making British products cheaper. India's share of world GDP fell from 27% to 2%. British industry grew fast with over 100 million Indian customers and no competition.""",
    """A British administrator admitted they taxed Indians to the utmost.
    Resentment grew. The 1857 Indian Rebellion resulted in over 800,000 Indian deaths.""",
    """The British government then took direct control, but paid the East India Company for the right to rule—essentially a self-dealing arrangement since many MPs were shareholders.""",
    """The Crown took over governance but kept the company's exploitative systems. The biggest problem was governing over 200 million people with only 6,000 officials and 70,000 European soldiers, plus 230,000 Indian troops paid by Indian taxes. The British never exceeded 0.5% of the population, so they feared unity.""",
    """To prevent that, they stoked Hindu‑Muslim hatred by segregating communities, creating land and food shortages to force competition, and restructuring politics along religious lines.""",
    """They made Muslims appear a threat by making them half of the army though only 20% of the population.""",
    """Simultaneously, they promoted the idea that India was historically Hindu and Muslims were foreign invaders—even though the British were the real invaders.""",
    """They denied Indians promotions.
    They paid them less.
    They Placed them under less competent British superiors.""",
    """Some Indians were anglicised through British education and joined the Indian Civil Service, which was 96% British.""",
    """That service was poorly run:
    Officials had too many tasks.
    They were evaluated only on tax collection.
    They ignored famine prevention or development.""",
    """British officials in India were paid more than those in England and lived isolated from Indian society, never considering India their home.""",
    """Small rebellions failed. So Indian elites founded the Indian National Congress (INC) in 1885 to advocate for Indian rights(They didn't advocate for independence yet)""",
    """They published 22 newspapers (India had 475 Indian‑owned by 1875) to expose corruption and foster unity.""",
    """They appealed for:
    Democracy
    Legislation protecting rights
    representation""",
    """But the British ignored them, evaluating officials only on revenue. Free speech was officially practiced but suppressed: newspapers were shut down, editors prosecuted.""",
    """After two decades of failure, frustrated nationalists realised that talking was useless. They concluded that if the British only cared about money.""",
    """They should make it hard to earn in India. They began boycotting British shops and directing customers to Indian ones. This peaceful protest worked, hurting British profits and getting attention for the first time.""",
    """Once upon a time there was this guy called Mahatma Gandhi. He was an indian lawyer.""",
    """he had used non‑violent resistance in South Africa(and he succeded) and returned to India in 1915.""",
    """He joined the INC and broadened its appeal beyond elites to ordinary Indians""",
    """he broadened its appeal by using speeches and sending news articles to Britain to expose atrocities.""",
    """During WWI (1914‑1918), over 1 million Indians served, and the British promised home rule (like Australia or Canada) in exchange.""",
    """But after the war, with 84,000 Indian dead and a famine killing millions, the British broke their promise. This caused massive resentment.""",
    """Millons of Indians were protesting so it was more than what the Brittish could handle""",
    """On April 9, 1919, the British arrested 2 nationalist leaders in Amritsar.""",
    """Protests escalated into riots with 15 deaths.""",
    """General Dyer arrived, banned gatherings of more than three people.""",
    """On April 13, 10,000‑15,000 people gathered for a spring festival, unaware of the ban.""",
    """Dyer ordered his troops to fire into the crowd, using 1,650 rounds, killing up to 1,500 civilians (Jallianwala Bagh massacre).""",
    """Dyer was forced to resign but received £1.6 million in donations, while victims' families got about £1,800 each.""",
    """This massacre became a rallying cry. Indians questioned British rule, the INC gained support, and the demand shifted from home rule to full independence.""",
    """In 1920, the INC launched the Non‑Cooperation Movement:
    Indians refused to work
    Indians broke unjust laws
    Indians used passive resistance (lying, giving wrong directions, deliberately wasting time)""",
    """The British arrested almost all INC leaders except Gandhi, expecting the movement to collapse. But protests continued""",
    """However, in 1922, a violent incident in Chauri Chaura where a police station was burned down shocked Gandhi.""",
    """He felt India was not ready for non‑violent independence and called off the movement, focusing on preparation instead.""",
    """The INC returned to seeking dominion status. They demonstrated economic damage through non‑cooperation. One famous protest was the 1930 Salt March: Gandhi walked 390 km to the coast to make illegal salt, breaking the British monopoly. Hundreds of thousands joined, making salt and buying/selling it, again making British control unworkable.""",
    """These protests forced the British to grant limited self‑governance in 1935 for about 10% of the population.""",
    """However, the British held elections with separate Hindu and Muslim electorates to prevent cooperation, favouring the Muslim League.""",
    """Though both groups resisted, division deepened.""",
    """The Muslim League began questioning whether Muslims should be a minority in a united India or have their own country (Pakistan).""",
    """In 1937, the INC won most seats, but real power remained with the British(feared the popularity and was told by lond to undermine the organization)""",
    """In 1939, WWII broke out. Britain brought India into the war without consulting Indian leaders. The INC was willing to support the war if home rule was granted, but the British refused.""",
    """The INC launched the Quit India Movement in 1942, demanding independence or withdrawal from the war.""",
    """The British brutally suppressed it, shut newspapers, and arrested the entire INC leadership.""",
    """The British then strengthened the Muslim League, giving it government positions and freedoms, hoping it would cause Hindu‑Muslim conflict.""",
    """The League grew from 112,000 members in 1941 to over 2 million by 1944.""",
    """Instead of fighting Hindus, the League advocated for an independent Pakistan.""",
    """After WWII, the British released INC leaders and held elections.""",
    """The League won most Muslim votes, strengthening the Pakistan demand.""",
    """Communal violence escalated. The British wanted to discredit the INC but now faced pressure from the US, USSR, China, and Afghanistan, and could not maintain order while recovering from war.""",
    """They decided to leave, believing India would collapse into civil war, after which they could return.""",
    """In February 1946, they began negotiations to hand over power. The INC and Muslim League could not agree on a united India.""",
    """The British set a deadline of June 1948, forcing a partition plan: Pakistan for Muslim‑majority provinces, India for the rest.""",
    """However, this left huge Hindu minorities in Pakistan and Muslim minorities in India, causing 14‑18 million people to move and up to 1 million deaths.""",
    """The regions of Punjab and Bengal, with mixed populations, were partitioned as well.""",
    """The 565 princely states were given the option to join either country, but the British also suggested they could become independent, which horrified everyone.""",
    """Most princes chose to join India or Pakistan""",
    """Although four (Hyderabad, Kashmir, Bhopal, Travancore) resisted and were eventually strong‑armed into joining.""",
    """Kashmir remains disputed between India, Pakistan, and China.""",
    """As violence grew, the British moved independence forward of India to August 15, 1947.""",
    """Both nations became secular states, and the Commonwealth of Nations was created to maintain diplomatic and trade ties.""",
    """Education before British Rule
    Education was traditional, rooted in culture, religion, and community life. Gurukuls, village pathshalas, and Muslim madrasas/maktabs were common. They taught Sanskrit, mathematics, astronomy, philosophy, medicine, arts, ethics, and good conduct; learning was oral, through listening, memorization, and practice, using local languages. Famous great learning centers like Nalanda and Takshashila attracted students from faraway lands. Many village children had access, though there were limits for girls and some social groups.""",
    """Education under British Rule
    A major shift came with Macaulay's Minute and the English Education Act of 1835: English became the main language of instruction, European science, literature, and history replaced much native learning, and Sanskrit and regional knowledge were neglected. Wood's Dispatch (1854) built a structured system, set up Education Departments, and opened Calcutta, Bombay, and Madras Universities in 1857.
    The main aim was creating an English-speaking class to work as clerks and administrators for the colonial government. Missionary and government schools spread slowly, mostly in towns; later Indians opened their own schools to preserve culture, and these ideas helped grow the movement for India's independence.
    “We must at present do our best to form a class who may be interpreters between us and the millions whom we govern — a class of persons Indian in blood and colour, but English in taste, in opinions, in morals, and in intellect.”
    — Thomas Babington Macaulay, Minute on Education (1835)""",
    """India is one of the most culturally complex and fascinating ecosystems on the planet. With a millennia-ohistory, the Indian subcontinent has not only given birth to some of the world's most influential religions, but it has also woven spirituality directly into the civic fabric, unwritten laws, and daily habits of its population. From an educational and pedagogical perspective, analysing India offers future English teachers an invaluable tool to foster critical intercultural competence and understand global diversity.""",
    """The Religious Landscape: Social and Identity Impact
    Hinduism: Practiced by nearly 80% of the population, it functions as an all-encompassing philosophy rather than a rigid, dogmatic institution. Core concepts such as dharma (cosmic duty) and karma (the universal law of cause and effect) govern ethical choices and daily behavior.
    Islam: Representing approximately 14% of the population, India is home to one of the largest Muslim communities globally. This presence has profoundly enriched the architectural, artistic, and linguistic heritage of the nation.
    Native Dharmic Religions and Minorities: The land is the birthplace of Buddhism, Jainism, and Sikhism, and hosts vibrant Christian and Parsi communities, demonstrating centuries of constant cultural syncretism.""",
    """Ancestral Customs and Sacred Symbols
    Animal Veneration: The protection of the cow is a powerful symbol of motherhood, non-violence (ahimsa), and the earth. Their free transit through hyper-modern metropolises visually illustrates the coexistence of economic progress and ancient sacred traditions.
    The Ganges River: Revered as the living goddess Ganga, millions of devotees gather annually at its banks in cities like Varanasi. The ritual baths and funerary practices performed there show an anthropological perspective where life, death, and purification interact naturally.""",
    """Major Festivals
    Celebrations structurally organise social life. Diwali (the festival of lights) celebrates the spiritual victory of light over darkness, while Holi (the festival of colors) welcomes spring, temporarily dissolving rigid social barriers and caste structures through shared joy.""",
    """Despite global modernization, this institution maintains overwhelming support, being the preference of 85% of the population over love marriages.""",
    """1. Selection Criteria and Filters
    The process is inherently pragmatic. It is based on filters designed to ensure cultural compatibility and long-term viability between families:
    Sociocultural Homogeneity: Religion and caste are non-negotiable primary filters to preserve heritage and customs. Additionally, the morality, educational level, and degree of conservatism of the families are evaluated.
    Astrology (Horoscope): Functions as an indispensable technical requirement. Vedic astrology (Guna Milap) is used to measure compatibility (requiring at least 18 out of 36 "gunas") and detect potential astrological obstacles like Mangalik Dosha.
    Gender Asymmetry in Evaluation: The scrutiny is markedly differentiated by gender. The man is evaluated almost exclusively on his professional status and ability to provide economic stability. The woman is judged primarily on her physical appearance (with a documented preference for fair skin) and her efficiency in domestic chores.""",
    """2. Approval Protocol
    The scrutiny subordinates individuality to family validation. After passing the astrological filter, the groom's family conducts an in-person inspection of the candidate. If both parties determine that the union is strategic and beneficial, the agreement is formalized through an engagement, setting the wedding date guided by astrological calendars.""",
    """3. Modernization of the Process
    Methods have evolved while the essence remains. Traditional matchmaking has been complemented by digital platforms and matchmaking software. In urban areas, criteria have adapted:
    Women's professional profiles are valued.
    Courtship periods are allowed prior to marriage to mitigate initial friction.
    Medical tests are required.
    Opposition to practices like dowry and child marriage is increasing.""",
    """4. Success Rate and Sociological Basis
    The model sustains its efficacy on a statistically minimal divorce rate (1 in 100). This long-term retention is attributed to arranged marriages being configured as a contract based on duty, mutual commitment, and family alignment rather than fleeting romantic passion.
    “Arranged marriages in India are not just unions of two individuals, but of two families, built on shared values and social harmony.”
    (Cultural Anthropologist, 2020)""",
    """Vegetation & Forests
    Fauna and Flora in India
    Vegetation
    The flora of India largely reflect the country's distribution of rainfall. Tropical broad- leaved evergreen and mixed, partially evergreen forests grow in areas with high precipitation; in successively less rainy areas are found moist and dry deciduous forests, scrub jungle, grassland, and desert vegetation. Coniferous forests are confined to the Himalayas. There are about 17,000 species of flowering plants in the country. The subcontinent's physical isolation, caused by its relief and climatic barriers, has resulted in a considerable number of endemic flora.""",
    """Roughly one- fourth of the country is forested. However, beginning in the late 20th century, forest depletion accelerated considerably to make room for more agriculture and urban- industrial development. That activity has taken its toll on many Indian plant species. About 20 species of higher-order plants are believed to have become extinct, and already some 1,300 species are considered to be endangered.""",
    """Tropical evergreen and mixed evergreen deciduous forests generally occupy areas with more than 80 inches (2,000 mm) of rainfall per year, mainly in upper Assam, the Western Ghats (especially in Kerala), parts of Odisha, and the Andaman and Nicobar Islands. Common trees in those tall multistoried forests include species of Mesua, Toona ciliata, Hopea, and Eugenia, as well as gurjun (Dipterocarpus turbinatus), which grows to heights exceeding 165 feet (50 meters) on the Andaman Islands and in Assam. The mixed evergreen- deciduous forests of Kerala and the Bengal Himalayas have a large variety of commercially valuable hardwood trees, of which Lagerstroemia lanceolata, East Indian, or Malabar, kino (Pterocarpus marsupium), and rosewood (Dalbergia latifolia) are well known.""",
    """Tropical moist deciduous forests generally occur in areas with 60 to 80 inches (1,500 to 2,000 mm) of rainfall, such as the northern part of the Eastern Ghats, east- central India, and western Karnataka. Dry deciduous forests, which grow in places receiving less than 60 inches (1,500 mm) of precipitation, characterize the subhumid and semiarid regions of Gujarat, Madhya Pradesh, eastern Rajasthan, central Andhra Pradesh, and western Tamil Nadu. Teak, sal (Shorea robusta), axle- wood (Anogeissus latifolia), tendu, ain, and Adina cardiifolia are some of the major deciduous species.""",
    """Tropical thorn forests occupy areas in various parts of the country, though mainly in the northern Gangetic Plain and southern peninsular India. Those forests generally grow in areas with less than 24 inches (600 mm) of rain but are also found in more humid areas, where deciduous forests have been degraded because of unregulated grazing, felling, and shifting agriculture. In those areas, such xerophytic (drought- tolerant) trees as species of acacia (babul and catechu) and Butea monosperma predominate.""",
    """The important commercial species include teak and sal. Teak, the foremost timber species, is largely confined to the peninsula. During the period of British rule, it was used extensively in shipbuilding, and certain forests were therefore reserved as teak plantations. Sal is confined to the lower Himalayas, Uttar Pradesh, Bihar, Jharkhand, Chhattisgarh, Assam, and Madhya Pradesh. Other species with commercial uses are sandalwood (Santalum album), the fragrant wood that is perhaps the most precious in the world, and rosewood, an evergreen used for carving and furniture""",
    """Many other species are noteworthy, some because of special ecological niches they occupy. Deltaic areas, for example, are fringed with mangrove forests, in which the dominant species—called sundri or sundari (Heritiera fomes), which is not, properly speaking, a mangrove—is characterized by respiratory roots that emerge from the tidal water. Conspicuous features of the tropical landscape are the palms, which are represented in India by some 100 species. Coconut and betel nut (the fruit of which is chewed) are cultivated mainly in coastal Karnataka and Kerala. Among the common, majestic- looking trees found throughout much of India are the mango—a major source of fruit—and two revered Ficus species, the pipal (famous as the Bo tree of the Buddha) and the banyan. Many types of bamboo (members of the grass family) grow over much of the country, with a concentration in the rainy areas.""",
    """Vegetation in the Himalayas can be generally divided into a number of elevation zones. Mixed evergreen- deciduous forests dominate the foothill areas up to a height of 5,000 feet (1,500 meters). Above that level subtropical pine forests make their appearance, followed by the Himalayan moist- temperate forests of oak, fir, deodar (Cedrus deodara), and spruce. The highest tree zone, consisting of alpine shrubs, is found up to an elevation of about 15,000 feet (4,500 meters). Rhododendrons are common at 12,000 feet (3,700 meters), above which occasional junipers and alpine meadows are encountered. Zones overlap considerably, and there are wide transitional bands.""",
    """India forms an important segment of what is known as the Oriental, or Sino- Indian, biogeographic region, which extends eastward from India to include mainland and much of insular Southeast Asia. Its fauna are numerous and highly diverse""",
    """Mammals, Birds, Reptiles, Fish, Insects & Conservation
    Mammals
    Mammals of the submontane region include Indian elephants (Elephas maximus)—associated from time immemorial with mythology and the splendor of regal pageantry—the great one- horned Indian rhinoceroses, a wide variety of ruminants, and various primates. There are also numerous predators represented by various genera.""",
    """Wild herds of elephants can be observed in several areas, particularly in such renowned national parks as Periyar Wildlife Sanctuary, in Kerala, and Bandipur, in Karnataka. The Indian rhinoceros is protected at Kaziranga National Park and Manas Wildlife Sanctuary in Assam.""",
    """Examples of ruminants include the wild Indian bison, or gaur (Bos gaurus), which inhabits peninsular forests; Indian buffalo; four- horned antelope (Tetracerus quadricornis), known locally as chousingha; blackbuck (Antilope cervicapra), or Indian antelope; antelope known as the nilgai (Boselaphus tragocamelus), or bluebuck; and Indian wild ass (Equus hemionus khur), or ghorkhar. There are also several species of deer, such as the rare Kashmir stag (hangul), swamp deer (barasingha), spotted deer, musk deer, brow- antlered deer (Cervus eldi eldi; an endangered species known locally as the sangai or thamin), and mouse deer.""",
    """Among the primates are various monkeys, including rhesus monkeys and gray, or Hanuman, langurs (Presbytis entellus), both of which are found in forested areas and near human settlements. The only ape found in India, the hoolock gibbon, is confined to the rainforests of the eastern region. Lion- tailed macaques of the Western Ghats, with halos of hair around their faces, are becoming rare because of poaching.""",
    """The country's carnivores include cats, dogs, foxes, jackals, and mongoose. Among the animals of prey, the Asiatic lion—now confined to Gir National Park, in the Kathiawar Peninsula of Gujarat—is the only extant subspecies of lion found outside of Africa. The majestic but endangered Bengal tiger, the national animal of India, is known for its rich color, illusive design, and formidable power. Of the five extant tiger subspecies worldwide, the Bengal tiger is the most numerous. Tigers are found in the forests of the Tarai region of northern India, Bihar, and Assam; the Ganges delta in West Bengal; the Eastern Ghats; Madhya Pradesh; and eastern Rajasthan. Once on the verge of extinction, Indian tigers have increased to several thousand, thanks largely to Project Tiger, which has established reserves in various parts of the country. Among other cats are leopards, clouded leopards, and various smaller species.""",
    """The Great Himalayas have notable fauna that includes wild sheep and goats, markhor (Capra falconeri), and ibex. Lesser pandas and snow leopards are also found in the upper reaches of the mountains.""",
    """Oxen, buffalo, horses, dromedary camels, sheep, goats, and pigs are common domesticated animals. The cattle breed Brahman, or zebu (Bos indicus), a species of ox, is an important draft animal.""",
    """Birds
    India has more than 1,200 species of birds and perhaps 2,000 subspecies, although some migratory species are found in the country only during the winter. The amount of avian life in the country represents roughly one- eighth of the world's species. The major reason for such a high level of diversity is the presence of a wide variety of habitats, from the cold and dry alpine tundra of Ladakh and Sikkim to the steamy, tangled jungles of the Sundarbans and wet, moist forests of the Western Ghats and the northeast. The country's many larger rivers provide deltas and backwaters for aquatic animal life, and many smaller rivers drain internally and end in vast saline lakes that are important breeding grounds for such birds as black- necked cranes (Grus nigricollis), barheaded geese (Anser indicus), and great crested grebes, as well as various kinds of terns, gulls, plovers, and sandpipers.""",
    """Herons, storks, ibises, and flamingos are well represented, and many of those birds frequent Keoladeo Ghana National Park, near Bharatpur, Rajasthan (designated a UNESCO World Heritage site in 1985). The Rann of Kachchh forms the nesting ground for one of the world's largest breeding colonies of flamingos.""",
    """Birds of prey include hawks, vultures, and eagles. Vultures are ubiquitous consumers of carrion. Game birds are represented by pheasants, jungle fowl, partridges, and quails. Peacocks (peafowl) are also common, especially in Gujarat and Rajasthan, where they are kept as pets. Respondently feathered, the peacock has been adopted as India's national bird.""",
    """Other notable birds in India include the Indian crane, commonly known as the sarus (Grus antigone); a large gray bird with crimson legs, the sarus stands as tall as a human. Bustards inhabit India's grasslands. The great Indian bustard (Ardeotis nigriceps), now confined to central and western India, is an endangered species protected by legislation. Sand grouse, pigeons, doves, parakeets, and cuckoos are found throughout the country. The mainly nonmigratory kingfisher, living close to water bodies, is considered sacred in many areas. Hornbills, barbets, and woodpeckers also are common, as are larks, crows, babblers, and thrushes.""",
    """Reptiles, fish, and insects
    Reptiles are well represented in India. Crocodiles inhabit the country's rivers, swamps, and lakes. The estuarine crocodile (Crocodilus porosus)—once attaining a maximum length of 30 feet (9 meters), though specimens exceeding 20 feet (6 meters) are now rare—usually lives on the fish, birds, and crabs of muddy deltaic regions. The long- snouted gavial, or gharial (Gavialis gangeticus), a species similar to the crocodile, is endemic to northern India; it is found in a number of large rivers, including the Ganges and Brahmaputra and their tributaries. Of the nearly 400 species of snakes, one- fifth are venomous. Kraits and cobras are particularly widespread venomous species. King cobras often grow to at least 12 feet (3.6 meters) long. The Indian python frequents marshy areas and grasslands. Lizards also are widespread, and turtles are found throughout India, especially along the eastern coast.""",
    """Of some 2,000 species of fish in India, about one- fifth live in fresh water. Common edible freshwater fish include catfish and several members of the carp family, notably the mahseer, which grows up to 6.5 feet (2 meters) and 200 pounds (90 kg). Sharks are found in India’s coastal waters and sometimes travel inland through major estuaries. Commercially valuable marine shellfish species include shrimps, prawns, crabs, lobsters, pearl oysters, and conchs.
    Among the commercially valuable insects are silkworms, bees, and the lac insect (Laccifer lacca). The latter secretes a sticky, resinous material called lac, from which shellac and a red dye are produced. Many other insects, such as various species of mosquitoes, are vectors for disease (e.g., malaria and yellow fever) or for human parasites (e.g., certain flatworms and nematodes).""",
    """Conservation
    The movement for the protection of forests and wildlife is strong in India. A number of species, including the elephant, rhinoceros, and tiger, have been declared endangered, and numerous others—both large and small—are considered vulnerable or at risk. Legislative measures have declared certain animals protected species, and areas with particularly rich floral diversity have been adopted as biosphere reserves. Virtually no forests are left in private hands. Projects likely to cause ecological damage must be cleared by the national government's Ministry of Environment, Forest, and Climate Change. Despite such measures, the reduced areas of forests, savannas, and grasslands provide little hope that India's population of animals can be restored to what it was at the end of the 19th century.""",
    """Government Public Schools of India
    They are free of charge, accessible to everyone, follow the national CBSE or state curriculum, use simple uniforms, and provide classes in both rural and urban areas:
    Funded by the State, for all children
    Light blue or light pink uniforms
    Sometimes students sit on the floor
    Use black chalkboards and work with basic supplies""",
    """Private Schools
    Better facilities, neat classrooms, formal uniforms, teach English and special subjects, and also follow the CBSE or ICSE curriculum:
    Monthly tuition fees
    Individual desks, proper lighting, good ventilation, computers
    Dark blue and white uniforms with ties
    Offer art and sports activities""",
    """Well‑known Universities and Institutes (IIT, Central Universities)
    Spacious classrooms, laboratories, libraries; university students learning together, carrying out projects and advanced studies:
    Higher professional education: engineering, medicine, science
    Study groups
    Teachers giving lessons in large lecture halls""",
    """What happens if caught cheating
    Strictly forbidden and punished seriously: exam paper cancelled, sometimes all subject results invalidated, must repeat full academic year, suspension. Serious cases face official penalties under anti-cheating laws. Marks become zero, certificate invalid, it delays moving up class or entering university.
    “Academic integrity is the foundation of India's education system — cheating is not tolerated at any level.”
    (University Grants Commission, India)"""
]

voice = PiperVoice.load("./en_US-lessac-medium.onnx")

for idx, text in enumerate(texts, start=1):
    filename = f"./vc/{idx:04d}.wav"
    with wave.open(filename, "wb") as wav_file:
        voice.synthesize_wav(text, wav_file)
    print(f"Generated {filename}")
