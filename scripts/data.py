from jinja2 import Template


class Video():
	""" Vic3 Event video class """

	def __init__(self):
		self.diplo = diplomatic.render()[4:]
		self.landscape = landscape.render()[4:]
		self.city = city.render()[4:]
		self.harbors = harbors.render()[4:]
		self.riot = riot.render()[4:]
		self.africa_animism = EventVideos["africa_animism"]
		self.africa_city_center = EventVideos["africa_city_center"]
		self.africa_construction_colony = EventVideos["africa_construction_colony"]
		self.africa_desert_expedition = EventVideos["africa_desert_expedition"]
		self.africa_diplomats_negotiating = EventVideos["africa_diplomats_negotiating"]
		self.africa_leader_arguing = EventVideos["africa_leader_arguing"]
		self.africa_prosperous_farm = EventVideos["africa_prosperous_farm"]
		self.africa_public_protest = EventVideos["africa_public_protest"]
		self.africa_soldiers_breaking_protest = EventVideos["africa_soldiers_breaking_protest"]
		self.asia_buddhism = EventVideos["asia_buddhism"]
		self.asia_confucianism_shinto = EventVideos["asia_confucianism_shinto"]
		self.asia_dead_cattle_poor_harvest = EventVideos["asia_dead_cattle_poor_harvest"]
		self.asia_factory_accident = EventVideos["asia_factory_accident"]
		self.asia_farmers_market = EventVideos["asia_farmers_market"]
		self.asia_hinduism_sikhism = EventVideos["asia_hinduism_sikhism"]
		self.asia_politician_parliament_motion = EventVideos["asia_politician_parliament_motion"]
		self.asia_poor_people_moving = EventVideos["asia_poor_people_moving"]
		self.asia_sepoy_mutiny = EventVideos["asia_sepoy_mutiny"]
		self.asia_union_leader = EventVideos["asia_union_leader"]
		self.asia_westerners_arriving = EventVideos["asia_westerners_arriving"]
		self.europenorthamerica_american_civil_war = EventVideos["europenorthamerica_american_civil_war"]
		self.europenorthamerica_antarctica = EventVideos["europenorthamerica_antarctica"]
		self.europenorthamerica_art_gallery = EventVideos["europenorthamerica_art_gallery"]
		self.europenorthamerica_before_the_battle = EventVideos["europenorthamerica_before_the_battle"]
		self.europenorthamerica_capitalists_meeting = EventVideos["europenorthamerica_capitalists_meeting"]
		self.europenorthamerica_gold_prospectors = EventVideos["europenorthamerica_gold_prospectors"]
		self.europenorthamerica_judaism = EventVideos["europenorthamerica_judaism"]
		self.europenorthamerica_london_center = EventVideos["europenorthamerica_london_center"]
		self.europenorthamerica_native_american = EventVideos["europenorthamerica_native_american"]
		self.europenorthamerica_opium_smoker = EventVideos["europenorthamerica_opium_smoker"]
		self.europenorthamerica_political_extremism = EventVideos["europenorthamerica_political_extremism"]
		self.europenorthamerica_rich_and_poor = EventVideos["europenorthamerica_rich_and_poor"]
		self.europenorthamerica_russian_serfs = EventVideos["europenorthamerica_russian_serfs"]
		self.europenorthamerica_springtime_of_nations = EventVideos["europenorthamerica_springtime_of_nations"]
		self.europenorthamerica_sufferage = EventVideos["europenorthamerica_sufferage"]
		self.middleeast_battlefield_trenches = EventVideos["middleeast_battlefield_trenches"]
		self.middleeast_courtroom_upheaval = EventVideos["middleeast_courtroom_upheaval"]
		self.middleeast_engineer_blueprint = EventVideos["middleeast_engineer_blueprint"]
		self.middleeast_islam = EventVideos["middleeast_islam"]
		self.middleeast_jungle_expedition = EventVideos["middleeast_jungle_expedition"]
		self.middleeast_middleclass_cafe = EventVideos["middleeast_middleclass_cafe"]
		self.middleeast_oil_derricks = EventVideos["middleeast_oil_derricks"]
		self.middleeast_police_breaking_door = EventVideos["middleeast_police_breaking_door"]
		self.middleeast_upperclass_party = EventVideos["middleeast_upperclass_party"]
		self.public_assasination_test = EventVideos["public_assasination_test"]
		self.southamerica_aristocrats = EventVideos["southamerica_aristocrats"]
		self.southamerica_child_labor = EventVideos["southamerica_child_labor"]
		self.southamerica_christianity = EventVideos["southamerica_christianity"]
		self.southamerica_election = EventVideos["southamerica_election"]
		self.southamerica_factory_opening = EventVideos["southamerica_factory_opening"]
		self.southamerica_public_figure_assassination = EventVideos["southamerica_public_figure_assassination"]
		self.southamerica_slave_chains = EventVideos["southamerica_slave_chains"]
		self.southamerica_slaves_night = EventVideos["southamerica_slaves_night"]
		self.southamerica_war_civilians = EventVideos["southamerica_war_civilians"]
		self.unspecific_airplane = EventVideos["unspecific_airplane"]
		self.unspecific_armored_train = EventVideos["unspecific_armored_train"]
		self.unspecific_automobile = EventVideos["unspecific_automobile"]
		self.unspecific_devastation = EventVideos["unspecific_devastation"]
		self.unspecific_factory_closed = EventVideos["unspecific_factory_closed"]
		self.unspecific_fire = EventVideos["unspecific_fire"]
		self.unspecific_gears_pistons = EventVideos["unspecific_gears_pistons"]
		self.unspecific_iceberg = EventVideos["unspecific_iceberg"]
		self.unspecific_military_parade = EventVideos["unspecific_military_parade"]
		self.unspecific_naval_battle = EventVideos["unspecific_naval_battle"]
		self.unspecific_politicians_arguing = EventVideos["unspecific_politicians_arguing"]
		self.unspecific_ruler_speaking_to_people = EventVideos["unspecific_ruler_speaking_to_people"]
		self.unspecific_sick_in_hospital = EventVideos["unspecific_sick_in_hospital"]
		self.unspecific_signed_contract = EventVideos["unspecific_signed_contract"]
		self.unspecific_steam_ship = EventVideos["unspecific_steam_ship"]
		self.unspecific_temperance_movement = EventVideos["unspecific_temperance_movement"]
		self.unspecific_trains = EventVideos["unspecific_trains"]
		self.unspecific_vandalized_storefront = EventVideos["unspecific_vandalized_storefront"]
		self.unspecific_whaling = EventVideos["unspecific_whaling"]
		self.unspecific_world_fair = EventVideos["unspecific_world_fair"]
		self.unspecific_airship = EventVideos["unspecific_airship"]

	def get(self, name: str):
		return EventVideos[name]


class Sound():
	""" Vic3 Event sound class """

	def __init__(self):
		self.harbors = EventSounds["harbors"]
		self.diplo = EventSounds["diplo"]
		self.city = EventSounds["city"]
		self.landscape = EventSounds["landscape"]
		self.africa_animism = EventSounds["africa_animism"]
		self.africa_city_center = EventSounds["africa_city_center"]
		self.africa_construction_colony = EventSounds["africa_construction_colony"]
		self.africa_desert_expedition = EventSounds["africa_desert_expedition"]
		self.africa_diplomats_negotiating = EventSounds["africa_diplomats_negotiating"]
		self.africa_leader_arguing = EventSounds["africa_leader_arguing"]
		self.africa_prosperous_farm = EventSounds["africa_prosperous_farm"]
		self.africa_public_protest = EventSounds["africa_public_protest"]
		self.africa_soldiers_breaking_protest = EventSounds["africa_soldiers_breaking_protest"]
		self.asia_buddhism = EventSounds["asia_buddhism"]
		self.asia_confucianism_shinto = EventSounds["asia_confucianism_shinto"]
		self.asia_dead_cattle_poor_harvest = EventSounds["asia_dead_cattle_poor_harvest"]
		self.asia_factory_accident = EventSounds["asia_factory_accident"]
		self.asia_farmers_market = EventSounds["asia_farmers_market"]
		self.asia_hinduism_sikhism = EventSounds["asia_hinduism_sikhism"]
		self.asia_politician_parliament_motion = EventSounds["asia_politician_parliament_motion"]
		self.asia_poor_people_moving = EventSounds["asia_poor_people_moving"]
		self.asia_sepoy_mutiny = EventSounds["asia_sepoy_mutiny"]
		self.asia_union_leader = EventSounds["asia_union_leader"]
		self.europenorthamerica_american_civil_war = EventSounds["europenorthamerica_american_civil_war"]
		self.europenorthamerica_before_the_battle = EventSounds["europenorthamerica_before_the_battle"]
		self.europenorthamerica_capitalists_meeting = EventSounds["europenorthamerica_capitalists_meeting"]
		self.europenorthamerica_gold_prospectors = EventSounds["europenorthamerica_gold_prospectors"]
		self.europenorthamerica_judaism = EventSounds["europenorthamerica_judaism"]
		self.europenorthamerica_london_center = EventSounds["europenorthamerica_london_center"]
		self.europenorthamerica_native_american = EventSounds["europenorthamerica_native_american"]
		self.europenorthamerica_opium_smoker = EventSounds["europenorthamerica_opium_smoker"]
		self.europenorthamerica_political_extremism = EventSounds["europenorthamerica_political_extremism"]
		self.europenorthamerica_rich_and_poor = EventSounds["europenorthamerica_rich_and_poor"]
		self.europenorthamerica_russian_serfs = EventSounds["europenorthamerica_russian_serfs"]
		self.europenorthamerica_slaves_breaking_their_chains = EventSounds["europenorthamerica_slaves_breaking_their_chains"]
		self.europenorthamerica_springtime_of_nations = EventSounds["europenorthamerica_springtime_of_nations"]
		self.europenorthamerica_sufferage = EventSounds["europenorthamerica_sufferage"]
		self.middleeast_battlefield_trenches = EventSounds["middleeast_battlefield_trenches"]
		self.middleeast_courtroom_upheaval = EventSounds["middleeast_courtroom_upheaval"]
		self.middleeast_engineer_blueprint = EventSounds["middleeast_engineer_blueprint"]
		self.middleeast_islam = EventSounds["middleeast_islam"]
		self.middleeast_jungle_expedition = EventSounds["middleeast_jungle_expedition"]
		self.middleeast_middleclass_cafe = EventSounds["middleeast_middleclass_cafe"]
		self.middleeast_oil_derricks = EventSounds["middleeast_oil_derricks"]
		self.middleeast_police_breaking_door = EventSounds["middleeast_police_breaking_door"]
		self.middleeast_upperclass_party = EventSounds["middleeast_upperclass_party"]
		self.misc_1Character_Banner = EventSounds["misc_1Character_Banner"]
		self.misc_2Characters = EventSounds["misc_2Characters"]
		self.southamerica_aristocrats = EventSounds["southamerica_aristocrats"]
		self.southamerica_child_labor = EventSounds["southamerica_child_labor"]
		self.southamerica_christianity = EventSounds["southamerica_christianity"]
		self.southamerica_election = EventSounds["southamerica_election"]
		self.southamerica_factory_opening = EventSounds["southamerica_factory_opening"]
		self.southamerica_public_figure_assassination = EventSounds["southamerica_public_figure_assassination"]
		self.southamerica_slaves_night = EventSounds["southamerica_slaves_night"]
		self.southamerica_war_civilians = EventSounds["southamerica_war_civilians"]
		self.unspecific_airplane = EventSounds["unspecific_airplane"]
		self.unspecific_airPlane = EventSounds["unspecific_airPlane"]
		self.unspecific_airship = EventSounds["unspecific_airship"]
		self.unspecific_arctic = EventSounds["unspecific_arctic"]
		self.unspecific_iceberg = EventSounds["unspecific_iceberg"]
		self.unspecific_armored_train = EventSounds["unspecific_armored_train"]
		self.unspecific_art_gallery = EventSounds["unspecific_art_gallery"]
		self.unspecific_automobile = EventSounds["unspecific_automobile"]
		self.unspecific_destruction = EventSounds["unspecific_destruction"]
		self.unspecific_fire = EventSounds["unspecific_fire"]
		self.unspecific_devastation = EventSounds["unspecific_devastation"]
		self.unspecific_factory_closed = EventSounds["unspecific_factory_closed"]
		self.unspecific_gears_pistons = EventSounds["unspecific_gears_pistons"]
		self.unspecific_iceberg_in_the_antartica = EventSounds["unspecific_iceberg_in_the_antartica"]
		self.unspecific_leader_speaking_to_a_group_of_people = EventSounds["unspecific_leader_speaking_to_a_group_of_people"]
		self.unspecific_ruler_speaking_to_people = EventSounds["unspecific_ruler_speaking_to_people"]
		self.unspecific_military_parade = EventSounds["unspecific_military_parade"]
		self.unspecific_naval_battle = EventSounds["unspecific_naval_battle"]
		self.unspecific_sick_people_in_a_field_hospital = EventSounds["unspecific_sick_people_in_a_field_hospital"]
		self.unspecific_sick_in_hospital = EventSounds["unspecific_sick_in_hospital"]
		self.unspecific_signed_contract = EventSounds["unspecific_signed_contract"]
		self.unspecific_steam_ship = EventSounds["unspecific_steam_ship"]
		self.unspecific_temperance_movement = EventSounds["unspecific_temperance_movement"]
		self.unspecific_trains = EventSounds["unspecific_trains"]
		self.unspecific_vandalized_storefront = EventSounds["unspecific_vandalized_storefront"]
		self.unspecific_whaling = EventSounds["unspecific_whaling"]
		self.unspecific_world_fair = EventSounds["unspecific_world_fair"]

	def get(self, name: str):
		return EventSounds[name]


class Icon():
	""" Vic3 Event icon class """

	def __init__(self):
		self.default = EventIcons["default"]
		self.election = EventIcons["election"]
		self.fire = EventIcons["fire"]
		self.industry = EventIcons["industry"]
		self.map = EventIcons["map"]
		self.military = EventIcons["military"]
		self.newspaper = EventIcons["newspaper"]
		self.portrait = EventIcons["portrait"]
		self.protest = EventIcons["protest"]
		self.scales = EventIcons["scales"]
		self.skull = EventIcons["skull"]
		self.trade = EventIcons["trade"]
		self.tutorial = EventIcons["tutorial"]
		self.book = EventIcons["book"]

	def get(self, name: str):
		return EventIcons[name]


EventIcons = {
	"default": "gfx/interface/icons/event_icons/event_default.dds",
	"election": "gfx/interface/icons/event_icons/event_election.dds",
	"fire": "gfx/interface/icons/event_icons/event_fire.dds",
	"industry": "gfx/interface/icons/event_icons/event_industry.dds",
	"map": "gfx/interface/icons/event_icons/event_map.dds",
	"military": "gfx/interface/icons/event_icons/event_military.dds",
	"newspaper": "gfx/interface/icons/event_icons/event_newspaper.dds",
	"portrait": "gfx/interface/icons/event_icons/event_portrait.dds",
	"protest": "gfx/interface/icons/event_icons/event_protest.dds",
	"scales": "gfx/interface/icons/event_icons/event_scales.dds",
	"skull": "gfx/interface/icons/event_icons/event_skull.dds",
	"trade": "gfx/interface/icons/event_icons/event_trade.dds",
	"tutorial": "gfx/interface/icons/event_icons/tutorial_icon.dds",
	"book": "gfx/interface/icons/event_icons/tutorial_icon.dds"
}

EventSounds = {
	"harbors": "event:/SFX/Events/unspecific/steam_ship",
	"diplo": "event:/SFX/Events/southamerica/aristocrats",
	"city": "event:/SFX/Events/africa/city_center",
	"landscape": "event:/SFX/Events/europenorthamerica/gold_prospectors",
	"africa_animism": "event:/SFX/Events/africa/animism",
	"africa_city_center": "event:/SFX/Events/africa/city_center",
	"africa_construction_colony": "event:/SFX/Events/africa/construction_colony",
	"africa_desert_expedition": "event:/SFX/Events/africa/desert_expedition",
	"africa_diplomats_negotiating": "event:/SFX/Events/africa/diplomats_negotiating",
	"africa_leader_arguing": "event:/SFX/Events/africa/leader_arguing",
	"africa_prosperous_farm": "event:/SFX/Events/africa/prosperous_farm",
	"africa_public_protest": "event:/SFX/Events/africa/public_protest",
	"africa_soldiers_breaking_protest": "event:/SFX/Events/africa/soldiers_breaking_protest",
	"asia_buddhism": "event:/SFX/Events/asia/buddhism",
	"asia_confucianism_shinto": "event:/SFX/Events/asia/confucianism_shinto",
	"asia_dead_cattle_poor_harvest": "event:/SFX/Events/asia/dead_cattle_poor_harvest",
	"asia_factory_accident": "event:/SFX/Events/asia/factory_accident",
	"asia_farmers_market": "event:/SFX/Events/asia/farmers_market",
	"asia_hinduism_sikhism": "event:/SFX/Events/asia/hinduism_sikhism",
	"asia_politician_parliament_motion": "event:/SFX/Events/asia/politician_parliament_motion",
	"asia_poor_people_moving": "event:/SFX/Events/asia/poor_people_moving",
	"asia_sepoy_mutiny": "event:/SFX/Events/asia/sepoy_mutiny",
	"asia_union_leader": "event:/SFX/Events/asia/union_leader",
	"europenorthamerica_american_civil_war": "event:/SFX/Events/europenorthamerica/american_civil_war",
	"europenorthamerica_before_the_battle": "event:/SFX/Events/europenorthamerica/before_the_battle",
	"europenorthamerica_capitalists_meeting": "event:/SFX/Events/europenorthamerica/capitalists_meeting",
	"europenorthamerica_gold_prospectors": "event:/SFX/Events/europenorthamerica/gold_prospectors",
	"europenorthamerica_judaism": "event:/SFX/Events/europenorthamerica/judaism",
	"europenorthamerica_london_center": "event:/SFX/Events/europenorthamerica/london_center",
	"europenorthamerica_native_american": "event:/SFX/Events/europenorthamerica/native_american",
	"europenorthamerica_opium_smoker": "event:/SFX/Events/europenorthamerica/opium_smoker",
	"europenorthamerica_political_extremism": "event:/SFX/Events/europenorthamerica/political_extremism",
	"europenorthamerica_rich_and_poor": "event:/SFX/Events/europenorthamerica/rich_and_poor",
	"europenorthamerica_russian_serfs": "event:/SFX/Events/europenorthamerica/russian_serfs",
	"europenorthamerica_slaves_breaking_their_chains": "event:/SFX/Events/europenorthamerica/slaves_breaking_their_chains",
	"europenorthamerica_springtime_of_nations": "event:/SFX/Events/europenorthamerica/springtime_of_nation",
	"europenorthamerica_sufferage": "event:/SFX/Events/europenorthamerica/sufferage",
	"middleeast_battlefield_trenches": "event:/SFX/Events/middleeast/battlefield_trenches",
	"middleeast_courtroom_upheaval": "event:/SFX/Events/middleeast/courtroom_upheaval",
	"middleeast_engineer_blueprint": "event:/SFX/Events/middleeast/engineer_blueprint",
	"middleeast_islam": "event:/SFX/Events/middleeast/islam",
	"middleeast_jungle_expedition": "event:/SFX/Events/middleeast/jungle_expedition",
	"middleeast_middleclass_cafe": "event:/SFX/Events/middleeast/middleclass_cafe",
	"middleeast_oil_derricks": "event:/SFX/Events/middleeast/oil_derricks",
	"middleeast_police_breaking_door": "event:/SFX/Events/middleeast/police_breaking_door",
	"middleeast_upperclass_party": "event:/SFX/Events/middleeast/upperclass_party",
	"misc_1Character_Banner": "event:/SFX/Events/misc/1Character_Banner",
	"misc_2Characters": "event:/SFX/Events/misc/2Characters",
	"southamerica_aristocrats": "event:/SFX/Events/southamerica/aristocrats",
	"southamerica_child_labor": "event:/SFX/Events/southamerica/child_labor",
	"southamerica_christianity": "event:/SFX/Events/southamerica/christianity",
	"southamerica_election": "event:/SFX/Events/southamerica/election",
	"southamerica_factory_opening": "event:/SFX/Events/southamerica/factory_opening",
	"southamerica_public_figure_assassination": "event:/SFX/Events/southamerica/public_figure_assassination",
	"southamerica_slaves_night": "event:/SFX/Events/southamerica/slaves_night",
	"southamerica_war_civilians": "event:/SFX/Events/southamerica/war_civilians",
	"unspecific_airplane": "event:/SFX/Events/unspecific/airplane",
	"unspecific_airPlane": "event:/SFX/Events/unspecific/airplane",
	"unspecific_airship": "event:/SFX/Events/unspecific/airship",
	"unspecific_arctic": "event:/SFX/Events/unspecific/arctic",
	"unspecific_iceberg": "event:/SFX/Events/unspecific/arctic",
	"unspecific_armored_train": "event:/SFX/Events/unspecific/armored_train",
	"unspecific_art_gallery": "event:/SFX/Events/unspecific/art_gallery",
	"unspecific_automobile": "event:/SFX/Events/unspecific/automobile",
	"unspecific_destruction": "event:/SFX/Events/unspecific/destruction",
	"unspecific_fire": "event:/SFX/Events/unspecific/destruction",
	"unspecific_devastation": "event:/SFX/Events/unspecific/devastation",
	"unspecific_factory_closed": "event:/SFX/Events/unspecific/factory_closed",
	"unspecific_gears_pistons": "event:/SFX/Events/unspecific/gears_pistons",
	"unspecific_iceberg_in_the_antartica": "event:/SFX/Events/unspecific/iceberg_in_the_antartica",
	"unspecific_leader_speaking_to_a_group_of_people": "event:/SFX/Events/unspecific/leader_speaking_to_a_group_of_people",
	"unspecific_ruler_speaking_to_people": "event:/SFX/Events/unspecific/leader_speaking_to_a_group_of_people",
	"unspecific_military_parade": "event:/SFX/Events/unspecific/military_parade",
	"unspecific_naval_battle": "event:/SFX/Events/unspecific/naval_battle",
	"unspecific_sick_people_in_a_field_hospital": "event:/SFX/Events/unspecific/sick_people_in_a_field_hospital",
	"unspecific_sick_in_hospital": "event:/SFX/Events/unspecific/sick_people_in_a_field_hospital",
	"unspecific_signed_contract": "event:/SFX/Events/unspecific/signed_contract",
	"unspecific_steam_ship": "event:/SFX/Events/unspecific/steam_ship",
	"unspecific_temperance_movement": "event:/SFX/Events/unspecific/temperance_movement",
	"unspecific_trains": "event:/SFX/Events/unspecific/trains",
	"unspecific_vandalized_storefront": "event:/SFX/Events/unspecific/vandalized_storefront",
	"unspecific_whaling": "event:/SFX/Events/unspecific/whaling",
	"unspecific_world_fair": "event:/SFX/Events/unspecific/world_fair"
}

EventVideos = {
	"africa_animism": "event_image = {\n\t\tvideo = \"gfx/event_pictures/africa_animism.bk2\"\n\t}",
	"africa_city_center": "event_image = {\n\t\tvideo = \"gfx/event_pictures/africa_city_center.bk2\"\n\t}",
	"africa_construction_colony": "event_image = {\n\t\tvideo = \"gfx/event_pictures/africa_construction_colony.bk2\"\n\t}",
	"africa_desert_expedition": "event_image = {\n\t\tvideo = \"gfx/event_pictures/africa_desert_expedition.bk2\"\n\t}",
	"africa_diplomats_negotiating": "event_image = {\n\t\tvideo = \"gfx/event_pictures/africa_diplomats_negotiating.bk2\"\n\t}",
	"africa_leader_arguing": "event_image = {\n\t\tvideo = \"gfx/event_pictures/africa_leader_arguing.bk2\"\n\t}",
	"africa_prosperous_farm": "event_image = {\n\t\tvideo = \"gfx/event_pictures/africa_prosperous_farm.bk2\"\n\t}",
	"africa_public_protest": "event_image = {\n\t\tvideo = \"gfx/event_pictures/africa_public_protest.bk2\"\n\t}",
	"africa_soldiers_breaking_protest": "event_image = {\n\t\tvideo = \"gfx/event_pictures/africa_soldiers_breaking_protest.bk2\"\n\t}",
	"asia_buddhism": "event_image = {\n\t\tvideo = \"gfx/event_pictures/asia_buddhism.bk2\"\n\t}",
	"asia_confucianism_shinto": "event_image = {\n\t\tvideo = \"gfx/event_pictures/asia_confucianism_shinto.bk2\"\n\t}",
	"asia_dead_cattle_poor_harvest": "event_image = {\n\t\tvideo = \"gfx/event_pictures/asia_dead_cattle_poor_harvest.bk2\"\n\t}",
	"asia_factory_accident": "event_image = {\n\t\tvideo = \"gfx/event_pictures/asia_factory_accident.bk2\"\n\t}",
	"asia_farmers_market": "event_image = {\n\t\tvideo = \"gfx/event_pictures/asia_farmers_market.bk2\"\n\t}",
	"asia_hinduism_sikhism": "event_image = {\n\t\tvideo = \"gfx/event_pictures/asia_hinduism_sikhism.bk2\"\n\t}",
	"asia_politician_parliament_motion": "event_image = {\n\t\tvideo = \"gfx/event_pictures/asia_politician_parliament_motion.bk2\"\n\t}",
	"asia_poor_people_moving": "event_image = {\n\t\tvideo = \"gfx/event_pictures/asia_poor_people_moving.bk2\"\n\t}",
	"asia_sepoy_mutiny": "event_image = {\n\t\tvideo = \"gfx/event_pictures/asia_sepoy_mutiny.bk2\"\n\t}",
	"asia_union_leader": "event_image = {\n\t\tvideo = \"gfx/event_pictures/asia_union_leader.bk2\"\n\t}",
	"asia_westerners_arriving": "event_image = {\n\t\tvideo = \"gfx/event_pictures/asia_westerners_arriving.bk2\"\n\t}",
	"europenorthamerica_american_civil_war": "event_image = {\n\t\tvideo = \"gfx/event_pictures/europenorthamerica_american_civil_war.bk2\"\n\t}",
	"europenorthamerica_antarctica": "event_image = {\n\t\tvideo = \"gfx/event_pictures/europenorthamerica_antarctica.bk2\"\n\t}",
	"europenorthamerica_art_gallery": "event_image = {\n\t\tvideo = \"gfx/event_pictures/europenorthamerica_art_gallery.bk2\"\n\t}",
	"europenorthamerica_before_the_battle": "event_image = {\n\t\tvideo = \"gfx/event_pictures/europenorthamerica_before_the_battle.bk2\"\n\t}",
	"europenorthamerica_capitalists_meeting": "event_image = {\n\t\tvideo = \"gfx/event_pictures/europenorthamerica_capitalists_meeting.bk2\"\n\t}",
	"europenorthamerica_gold_prospectors": "event_image = {\n\t\tvideo = \"gfx/event_pictures/europenorthamerica_gold_prospectors.bk2\"\n\t}",
	"europenorthamerica_judaism": "event_image = {\n\t\tvideo = \"gfx/event_pictures/europenorthamerica_judaism.bk2\"\n\t}",
	"europenorthamerica_london_center": "event_image = {\n\t\tvideo = \"gfx/event_pictures/europenorthamerica_london_center.bk2\"\n\t}",
	"europenorthamerica_native_american": "event_image = {\n\t\tvideo = \"gfx/event_pictures/europenorthamerica_native_american.bk2\"\n\t}",
	"europenorthamerica_opium_smoker": "event_image = {\n\t\tvideo = \"gfx/event_pictures/europenorthamerica_opium_smoker.bk2\"\n\t}",
	"europenorthamerica_political_extremism": "event_image = {\n\t\tvideo = \"gfx/event_pictures/europenorthamerica_political_extremism.bk2\"\n\t}",
	"europenorthamerica_rich_and_poor": "event_image = {\n\t\tvideo = \"gfx/event_pictures/europenorthamerica_rich_and_poor.bk2\"\n\t}",
	"europenorthamerica_russian_serfs": "event_image = {\n\t\tvideo = \"gfx/event_pictures/europenorthamerica_russian_serfs.bk2\"\n\t}",
	"europenorthamerica_springtime_of_nations": "event_image = {\n\t\tvideo = \"gfx/event_pictures/europenorthamerica_springtime_of_nations.bk2\"\n\t}",
	"europenorthamerica_sufferage": "event_image = {\n\t\tvideo = \"gfx/event_pictures/europenorthamerica_sufferage.bk2\"\n\t}",
	"middleeast_battlefield_trenches": "event_image = {\n\t\tvideo = \"gfx/event_pictures/middleeast_battlefield_trenches.bk2\"\n\t}",
	"middleeast_courtroom_upheaval": "event_image = {\n\t\tvideo = \"gfx/event_pictures/middleeast_courtroom_upheaval.bk2\"\n\t}",
	"middleeast_engineer_blueprint": "event_image = {\n\t\tvideo = \"gfx/event_pictures/middleeast_engineer_blueprint.bk2\"\n\t}",
	"middleeast_islam": "event_image = {\n\t\tvideo = \"gfx/event_pictures/middleeast_islam.bk2\"\n\t}",
	"middleeast_jungle_expedition": "event_image = {\n\t\tvideo = \"gfx/event_pictures/middleeast_jungle_expedition.bk2\"\n\t}",
	"middleeast_middleclass_cafe": "event_image = {\n\t\tvideo = \"gfx/event_pictures/middleeast_middleclass_cafe.bk2\"\n\t}",
	"middleeast_oil_derricks": "event_image = {\n\t\tvideo = \"gfx/event_pictures/middleeast_oil_derricks.bk2\"\n\t}",
	"middleeast_police_breaking_door": "event_image = {\n\t\tvideo = \"gfx/event_pictures/middleeast_police_breaking_door.bk2\"\n\t}",
	"middleeast_upperclass_party": "event_image = {\n\t\tvideo = \"gfx/event_pictures/middleeast_upperclass_party.bk2\"\n\t}",
	"public_assasination_test": "event_image = {\n\t\tvideo = \"gfx/event_pictures/public_assasination_test.bk2\"\n\t}",
	"southamerica_aristocrats": "event_image = {\n\t\tvideo = \"gfx/event_pictures/southamerica_aristocrats.bk2\"\n\t}",
	"southamerica_child_labor": "event_image = {\n\t\tvideo = \"gfx/event_pictures/southamerica_child_labor.bk2\"\n\t}",
	"southamerica_christianity": "event_image = {\n\t\tvideo = \"gfx/event_pictures/southamerica_christianity.bk2\"\n\t}",
	"southamerica_election": "event_image = {\n\t\tvideo = \"gfx/event_pictures/southamerica_election.bk2\"\n\t}",
	"southamerica_factory_opening": "event_image = {\n\t\tvideo = \"gfx/event_pictures/southamerica_factory_opening.bk2\"\n\t}",
	"southamerica_public_figure_assassination": "event_image = {\n\t\tvideo = \"gfx/event_pictures/southamerica_public_figure_assassination.bk2\"\n\t}",
	"southamerica_slave_chains": "event_image = {\n\t\tvideo = \"gfx/event_pictures/southamerica_slave_chains.bk2\"\n\t}",
	"southamerica_slaves_night": "event_image = {\n\t\tvideo = \"gfx/event_pictures/southamerica_slaves_night.bk2\"\n\t}",
	"southamerica_war_civilians": "event_image = {\n\t\tvideo = \"gfx/event_pictures/southamerica_war_civilians.bk2\"\n\t}",
	"unspecific_airPlane": "event_image = {\n\t\tvideo = \"gfx/event_pictures/unspecific_airPlane.bk2\"\n\t}",
	"unspecific_airplane": "event_image = {\n\t\tvideo = \"gfx/event_pictures/unspecific_airPlane.bk2\"\n\t}",
	"unspecific_armored_train": "event_image = {\n\t\tvideo = \"gfx/event_pictures/unspecific_armored_train.bk2\"\n\t}",
	"unspecific_automobile": "event_image = {\n\t\tvideo = \"gfx/event_pictures/unspecific_automobile.bk2\"\n\t}",
	"unspecific_devastation": "event_image = {\n\t\tvideo = \"gfx/event_pictures/unspecific_devastation.bk2\"\n\t}",
	"unspecific_factory_closed": "event_image = {\n\t\tvideo = \"gfx/event_pictures/unspecific_factory_closed.bk2\"\n\t}",
	"unspecific_fire": "event_image = {\n\t\tvideo = \"gfx/event_pictures/unspecific_fire.bk2\"\n\t}",
	"unspecific_gears_pistons": "event_image = {\n\t\tvideo = \"gfx/event_pictures/unspecific_gears_pistons.bk2\"\n\t}",
	"unspecific_iceberg": "event_image = {\n\t\tvideo = \"gfx/event_pictures/unspecific_iceberg.bk2\"\n\t}",
	"unspecific_military_parade": "event_image = {\n\t\tvideo = \"gfx/event_pictures/unspecific_military_parade.bk2\"\n\t}",
	"unspecific_naval_battle": "event_image = {\n\t\tvideo = \"gfx/event_pictures/unspecific_naval_battle.bk2\"\n\t}",
	"unspecific_politicians_arguing": "event_image = {\n\t\tvideo = \"gfx/event_pictures/unspecific_politicians_arguing.bk2\"\n\t}",
	"unspecific_ruler_speaking_to_people": "event_image = {\n\t\tvideo = \"gfx/event_pictures/unspecific_ruler_speaking_to_people.bk2\"\n\t}",
	"unspecific_sick_in_hospital": "event_image = {\n\t\tvideo = \"gfx/event_pictures/unspecific_sick_in_hospital.bk2\"\n\t}",
	"unspecific_signed_contract": "event_image = {\n\t\tvideo = \"gfx/event_pictures/unspecific_signed_contract.bk2\"\n\t}",
	"unspecific_steam_ship": "event_image = {\n\t\tvideo = \"gfx/event_pictures/unspecific_steam_ship.bk2\"\n\t}",
	"unspecific_temperance_movement": "event_image = {\n\t\tvideo = \"gfx/event_pictures/unspecific_temperance_movement.bk2\"\n\t}",
	"unspecific_trains": "event_image = {\n\t\tvideo = \"gfx/event_pictures/unspecific_trains.bk2\"\n\t}",
	"unspecific_vandalized_storefront": "event_image = {\n\t\tvideo = \"gfx/event_pictures/unspecific_vandalized_storefront.bk2\"\n\t}",
	"unspecific_whaling": "event_image = {\n\t\tvideo = \"gfx/event_pictures/unspecific_whaling.bk2\"\n\t}",
	"unspecific_world_fair": "event_image = {\n\t\tvideo = \"gfx/event_pictures/unspecific_world_fair.bk2\"\n\t}",
	"unspecific_airship": "event_image = {\n\t\tvideo = \"gfx/event_pictures/unspecififc_airship.bk2\"\n\t}",
}

GuiWindows = {
	"1char_tab": "event_window_1char_tabloid",
	"1char_lord": "event_window_1char_lord_kitchener",
	"1char_propaganda": "event_window_1char_propaganda",
	"2char": "event_window_2char",
	"big_icon": "event_window_big_icon_center",
}

landscape = Template('''pdx
event_image = { trigger = { var:picture = 1 } texture = "gfx/event_pictures/paintings/landscapes/Albert_Bierstadt_A_Storm_in_the_Rocky_Mountains_Mt_Rosalie.dds" }
	event_image = { trigger = { var:picture = 2 } texture = "gfx/event_pictures/paintings/landscapes/Albert_Bierstadt_Puget_Sound_on_the_Pacific_Coast.dds" }
	event_image = { trigger = { var:picture = 3 } texture = "gfx/event_pictures/paintings/landscapes/Albert_Bierstadt_Valley_of_the_Yosemite.dds" }
	event_image = { trigger = { var:picture = 4 } texture = "gfx/event_pictures/paintings/landscapes/Asher_Brown_Durand_The_Catskills.dds" }
	event_image = { trigger = { var:picture = 5 } texture = "gfx/event_pictures/paintings/landscapes/Asher_Durand_Kindred_Spirits.dds" }
	event_image = { trigger = { var:picture = 6 } texture = "gfx/event_pictures/paintings/landscapes/A_Bit_of_the_Roman_Aqueduct.dds" }
	event_image = { trigger = { var:picture = 7 } texture = "gfx/event_pictures/paintings/landscapes/Caspar_David_Friedrich_Cairn_in_Snow.dds" }
	event_image = { trigger = { var:picture = 8 } texture = "gfx/event_pictures/paintings/landscapes/Caspar_David_Friedrich_Der_einsame_Baum.dds" }
	event_image = { trigger = { var:picture = 9 } texture = "gfx/event_pictures/paintings/landscapes/Caspar_David_Friedrich_Morgen_im_Riesengebirge.dds" }
	event_image = { trigger = { var:picture = 10 } texture = "gfx/event_pictures/paintings/landscapes/Church_Heart_of_the_Andes.dds" }
	event_image = { trigger = { var:picture = 11 } texture = "gfx/event_pictures/paintings/landscapes/Cole_Thomas_Arch_of_Nero_1846.dds" }
	event_image = { trigger = { var:picture = 12 } texture = "gfx/event_pictures/paintings/landscapes/Cole_Thomas_Genesee_Scenery_1847.dds" }
	event_image = { trigger = { var:picture = 13 } texture = "gfx/event_pictures/paintings/landscapes/Cole_Thomas_Lake_with_Dead_Trees.dds" }
	event_image = { trigger = { var:picture = 14 } texture = "gfx/event_pictures/paintings/landscapes/Cole_Thomas_The_Oxbow.dds" }
	event_image = { trigger = { var:picture = 15 } texture = "gfx/event_pictures/paintings/landscapes/Constable_Stratford_Mill.dds" }
	event_image = { trigger = { var:picture = 16 } texture = "gfx/event_pictures/paintings/landscapes/Frederic_Edwin_Church_The_Andes_of_Ecuador.dds" }
	event_image = { trigger = { var:picture = 17 } texture = "gfx/event_pictures/paintings/landscapes/Frogner_Manor_by_I_C_Dahl_for_Benjamin_Wegner.dds" }
	event_image = { trigger = { var:picture = 18 } texture = "gfx/event_pictures/paintings/landscapes/George_Inness_The_Lackawanna_Valley.dds" }
	event_image = { trigger = { var:picture = 19 } texture = "gfx/event_pictures/paintings/landscapes/John_Constable_Golding_Constables_Flower_Garden.dds" }
	event_image = { trigger = { var:picture = 20 } texture = "gfx/event_pictures/paintings/landscapes/John_Constable_The_Hay_Wain.dds" }
	event_image = { trigger = { var:picture = 21 } texture = "gfx/event_pictures/paintings/landscapes/John_Constable_Wivenhoe_Park.dds" }
	event_image = { trigger = { var:picture = 22 } texture = "gfx/event_pictures/paintings/landscapes/Karl_Friedrich_Schinkel_Gotischer_Dom_am_Wasser.dds" }
	event_image = { trigger = { var:picture = 23 } texture = "gfx/event_pictures/paintings/landscapes/Kensett_John_F_Lake_George.dds" }
	event_image = { trigger = { var:picture = 24 } texture = "gfx/event_pictures/paintings/landscapes/Landscape_with_Rainbow.dds" }
	event_image = { trigger = { var:picture = 25 } texture = "gfx/event_pictures/paintings/landscapes/Looking_Down_Yosemite_Valley.dds" }
	event_image = { trigger = { var:picture = 26 } texture = "gfx/event_pictures/paintings/landscapes/rockymountains.dds" }
	event_image = { trigger = { var:picture = 27 } texture = "gfx/event_pictures/paintings/landscapes/The_Subsiding_of_the_Waters_of_the_Deluge.dds" }
	event_image = { trigger = { var:picture = 28 } texture = "gfx/event_pictures/paintings/landscapes/The_Valley_of_Wyoming.dds" }
	event_image = { trigger = { var:picture = 29 } texture = "gfx/event_pictures/paintings/landscapes/The_White_Horse_by_John_Constable.dds" }
	event_image = { trigger = { var:picture = 30 } texture = "gfx/event_pictures/paintings/landscapes/Thomas_Cole_Il_Penseroso.dds" }
	event_image = { trigger = { var:picture = 31 } texture = "gfx/event_pictures/paintings/landscapes/Twilight_in_the_Wilderness_by_Frederic_Edwin_Church.dds" }
	event_image = { trigger = { var:picture = 32 } texture = "gfx/event_pictures/paintings/landscapes/View_of_Fort_Putnam.dds" }
	event_image = { trigger = { var:picture = 33 } texture = "gfx/event_pictures/paintings/landscapes/westernfrontier.dds" }
	event_image = { trigger = { var:picture = 34 } texture = "gfx/event_pictures/paintings/landscapes/yosemete.dds" }
''')

diplomatic = Template('''pdx
event_image = {
		trigger = {
			ruler.religion = {
				OR = {
					this = sunni
					this = shiite
				}
			}
		}
		video = "gfx/event_pictures/middleeast_upperclass_party.bk2"
	}
	event_image = {
		trigger = {
			ruler.culture = {
				OR = {
					has_discrimination_trait = iberian_culture_group
					has_discrimination_trait = lusophone
					has_discrimination_trait = hispanophone
				}
			}
		}
		video = "gfx/event_pictures/southamerica_aristocrats.bk2"
	}
	event_image = { trigger = { ruler.culture = { has_culture_graphics = african } } video = "gfx/event_pictures/africa_diplomats_negotiating.bk2" }
	event_image = { trigger = { ruler.culture = { has_culture_graphics = asian } } video = "gfx/event_pictures/asia_politician_parliament_motion.bk2" }
	event_image = { trigger = { ruler.culture = { has_culture_graphics = european } } video = "gfx/event_pictures/europenorthamerica_capitalists_meeting.bk2" }
	event_image = { trigger = { ruler.culture = { has_culture_graphics = mideast_indian } } video = "gfx/event_pictures/asia_politician_parliament_motion.bk2" }
''')

city = Template('''pdx
event_image = { trigger = { var:picture = 1 } texture = "gfx/event_pictures/paintings/cities/An_Overshot_Mill_in_Wales_James_Ward.dds" }
	event_image = { trigger = { var:picture = 2 } texture = "gfx/event_pictures/paintings/cities/Cole_Thomas_View_of_Florence_from_San_Miniato_1837.dds" }
	event_image = { trigger = { var:picture = 3 } texture = "gfx/event_pictures/paintings/cities/The_945_Accommodation.dds" }
	event_image = { trigger = { var:picture = 4 } texture = "gfx/event_pictures/paintings/cities/Thomas_Cole_Architects_Dream.dds" }
	event_image = { trigger = { var:picture = 5 } texture = "gfx/event_pictures/paintings/cities/Thomas_Malton_the_Younger_High_Street_Oxford.dds" }
	event_image = { trigger = { var:picture = 6 } texture = "gfx/event_pictures/paintings/cities/Venise_La_Piazetta.dds" }
''')

harbors = Template('''pdx
event_image = { trigger = { var:picture = 1 } texture = "gfx/event_pictures/paintings/harbors/Fitz_Henry_Lane_Castine_Harbor_and_Town.dds" }
	event_image = { trigger = { var:picture = 2 } texture = "gfx/event_pictures/paintings/harbors/San_Diego.dds" }
	event_image = { trigger = { var:picture = 3 } texture = "gfx/event_pictures/paintings/harbors/Stage_Fort_across_Gloucester_Harbor.dds" }
	event_image = { trigger = { var:picture = 4 } texture = "gfx/event_pictures/paintings/harbors/The_Golden_State_Entering_New_York_Harbor.dds" }
	event_image = { trigger = { var:picture = 5 } texture = "gfx/event_pictures/paintings/harbors/The_Paying_out_Machinery_in_the_Stern_of_the_Great_Eastern.dds" }
	event_image = { trigger = { var:picture = 6 } texture = "gfx/event_pictures/paintings/harbors/The_Russian_Ship_of_the_Line_Asow_and_a_Frigate_at_Anchor_in_the_Roads_of_Elsinore.dds" }
	event_image = { trigger = { var:picture = 7 } texture = "gfx/event_pictures/paintings/harbors/View_from_the_Quai_dOrsay.dds" }
''')

riot = Template('''pdx
event_image = {
		trigger = {
			ruler.religion = {
				OR = {
					this = sunni
					this = shiite
				}
			}
		}
		video = "gfx/event_pictures/middleeast_courtroom_upheaval.bk2"
	}
	event_image = {
		trigger = {
			ruler.culture = {
				OR = {
					has_discrimination_trait = iberian_culture_group
					has_discrimination_trait = lusophone
					has_discrimination_trait = hispanophone
				}
			}
		}
		video = "gfx/event_pictures/southamerica_war_civilians.bk2"
	}
	event_image = { trigger = { ruler.culture = { has_culture_graphics = african } } video = "gfx/event_pictures/africa_public_protest.bk2" }
	event_image = { trigger = { ruler.culture = { has_culture_graphics = asian } } video = "gfx/event_pictures/asia_union_leader.bk2" }
	event_image = { trigger = { ruler.culture = { has_culture_graphics = european } } video = "gfx/event_pictures/europenorthamerica_springtime_of_nations.bk2" }
	event_image = { trigger = { ruler.culture = { has_culture_graphics = mideast_indian } } video = "gfx/event_pictures/asia_sepoy_mutiny.bk2" }
''')