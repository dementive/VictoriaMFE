from jinja2 import Template


class EventImage():
	""" Victoria 3 Event video and texture class """

	def __init__(self):
		self.diplo = diplomatic.render()[4:]
		self.landscape = landscape.render()[4:]
		self.city = city.render()[4:]
		self.harbors = harbors.render()[4:]
		self.riot = riot.render()[4:]
		self.industry = industry.render()[4:]

		self.ironclad = EventVideos["ironclad"]
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
	""" Victoria 3 Event sound class """

	def __init__(self):
		self.industry = EventSounds["industry"]
		self.ironclad = EventSounds["ironclad"]
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
	""" Victoria 3 Event icon class """

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
		self.academics = EventIcons["academics"]
		self.active_peace_deal = EventIcons["active_peace_deal"]
		self.aristocrats = EventIcons["aristocrats"]
		self.fabric_roll = EventIcons["fabric_roll"]
		self.gemstone = EventIcons["gemstone"]
		self.armillary = EventIcons["armillary"]
		self.bell = EventIcons["bell"]
		self.bureaucrats = EventIcons["bureaucrats"]
		self.capitalists = EventIcons["capitalists"]
		self.character_busy = EventIcons["character_busy"]
		self.clergymen = EventIcons["clergymen"]
		self.clerks = EventIcons["clerks"]
		self.diplomatic_play = EventIcons["diplomatic_play"]
		self.economic_dominance = EventIcons["economic_dominance"]
		self.egalitarian_society = EventIcons["egalitarian_society"]
		self.engineers = EventIcons["engineers"]
		self.farmers = EventIcons["farmers"]
		self.force_recognition = EventIcons["force_recognition"]
		self.has_no_research = EventIcons["has_no_research"]
		self.hegemon = EventIcons["hegemon"]
		self.icon_kill = EventIcons["icon_kill"]
		self.laborers = EventIcons["laborers"]
		self.legitimacy = EventIcons["legitimacy"]
		self.literacy = EventIcons["literacy"]
		self.machinists = EventIcons["machinists"]
		self.market_isolated = EventIcons["market_isolated"]
		self.officers = EventIcons["officers"]
		self.peasants = EventIcons["peasants"]
		self.power_projection = EventIcons["power_projection"]
		self.raid_convoys = EventIcons["raid_convoys"]
		self.shopkeepers = EventIcons["shopkeepers"]
		self.slaves = EventIcons["slaves"]
		self.soldiers = EventIcons["soldiers"]
		self.standby = EventIcons["standby"]
		self.supply_low = EventIcons["supply_low"]
		self.take_colony = EventIcons["take_colony"]
		self.take_treaty_port = EventIcons["take_treaty_port"]
		self.tutorial_icon = EventIcons["tutorial_icon"]
		self.unit_attack = EventIcons["unit_attack"]
		self.unit_defense = EventIcons["unit_defense"]
		self.war_reparations = EventIcons["war_reparations"]
		self.wasted_construction = EventIcons["wasted_construction"]
		self.academia = EventIcons["academia"]
		self.aeroplanes = EventIcons["aeroplanes"]
		self.analytical_philosophy = EventIcons["analytical_philosophy"]
		self.anarchy = EventIcons["anarchy"]
		self.army_reserves = EventIcons["army_reserves"]
		self.automobiles = EventIcons["automobiles"]
		self.banking = EventIcons["banking"]
		self.bureaucracy = EventIcons["bureaucracy"]
		self.canneries = EventIcons["canneries"]
		self.central_archives = EventIcons["central_archives"]
		self.combustion_engine = EventIcons["combustion_engine"]
		self.compression_ignition = EventIcons["compression_ignition"]
		self.currency_standards = EventIcons["currency_standards"]
		self.democracy = EventIcons["democracy"]
		self.enlistment_offices = EventIcons["enlistment_offices"]
		self.film = EventIcons["film"]
		self.fine_art = EventIcons["fine_art"]
		self.food = EventIcons["food"]
		self.human_rights = EventIcons["human_rights"]
		self.hydraulic_cranes = EventIcons["hydraulic_cranes"]
		self.international_diplomacy = EventIcons["international_diplomacy"]
		self.international_exchange_standards = EventIcons["international_exchange_standards"]
		self.international_trade = EventIcons["international_trade"]
		self.labor_movement = EventIcons["labor_movement"]
		self.lathe = EventIcons["lathe"]
		self.law_enforcement = EventIcons["law_enforcement"]
		self.lightbulbs = EventIcons["lightbulbs"]
		self.line_infantry = EventIcons["line_infantry"]
		self.literature = EventIcons["literature"]
		self.locomotives = EventIcons["locomotives"]
		self.macroeconomics = EventIcons["macroeconomics"]
		self.manufacturies = EventIcons["manufacturies"]
		self.mass_propaganda = EventIcons["mass_propaganda"]
		self.mass_surveillance = EventIcons["mass_surveillance"]
		self.mechanized_farming = EventIcons["mechanized_farming"]
		self.military_aviation = EventIcons["military_aviation"]
		self.military_statistics = EventIcons["military_statistics"]
		self.nationalism = EventIcons["nationalism"]
		self.navigation = EventIcons["navigation"]
		self.paddle_steamer = EventIcons["paddle_steamer"]
		self.pan_nationalism = EventIcons["pan_nationalism"]
		self.paper = EventIcons["paper"]
		self.philosophical_pragmatism = EventIcons["philosophical_pragmatism"]
		self.political_agitation = EventIcons["political_agitation"]
		self.postal_savings = EventIcons["postal_savings"]
		self.power_of_the_purse = EventIcons["power_of_the_purse"]
		self.prospecting_tech = EventIcons["prospecting_tech"]
		self.psychoanalysis = EventIcons["psychoanalysis"]
		self.pumpjacks = EventIcons["pumpjacks"]
		self.radio = EventIcons["radio"]
		self.railways = EventIcons["railways"]
		self.rationalism = EventIcons["rationalism"]
		self.realism = EventIcons["realism"]
		self.sea_lane_strategies = EventIcons["sea_lane_strategies"]
		self.shift_work = EventIcons["shift_work"]
		self.socialism = EventIcons["socialism"]
		self.standing_army = EventIcons["standing_army"]
		self.steam_donkey = EventIcons["steam_donkey"]
		self.steelworking = EventIcons["steelworking"]
		self.stock_exchanges = EventIcons["stock_exchanges"]
		self.tools = EventIcons["tools"]
		self.urbanization = EventIcons["urbanization"]
		self.zeppelins = EventIcons["zeppelins"]
		self.clippers = EventIcons["clippers"]
		self.drydock = EventIcons["drydock"]
		self.electrical_capacitors = EventIcons["electrical_capacitors"]
		self.electrical_generation = EventIcons["electrical_generation"]
		self.ironclads = EventIcons["ironclads"]
		self.man_o_wars = EventIcons["man_o_wars"]
		self.oil = EventIcons["oil"]
		self.opium = EventIcons["opium"]
		self.paddle_steamer = EventIcons["paddle_steamer"]
		self.porcelain = EventIcons["porcelain"]
		self.psychiatry = EventIcons["psychiatry"]
		self.rubber = EventIcons["rubber"]
		self.screw_frigate = EventIcons["screw_frigate"]
		self.shaft_mining = EventIcons["shaft_mining"]
		self.shell_gun = EventIcons["shell_gun"]
		self.steamers = EventIcons["steamers"]
		self.steel_railway_cars = EventIcons["steel_railway_cars"]
		self.telephones = EventIcons["telephones"]
		self.transportation = EventIcons["transportation"]
		self.war_propaganda = EventIcons["war_propaganda"]
		self.wargaming = EventIcons["wargaming"]
		self.watertube_boiler = EventIcons["watertube_boiler"]
		self.wine = EventIcons["wine"]
		self.ammunition = EventIcons["ammunition"]
		self.artillery = EventIcons["artillery"]
		self.breech_loading_artillery = EventIcons["breech_loading_artillery"]
		self.dreadnought = EventIcons["dreadnought"]
		self.military_drill = EventIcons["military_drill"]
		self.destroyers = EventIcons["destroyers"]
		self.mobile_armor = EventIcons["mobile_armor"]
		self.monitor_tech = EventIcons["monitor_tech"]
		self.luxury_clothes = EventIcons["luxury_clothes"]

	def get(self, name: str):
		return EventIcons[name]


class GuiWindow():
	""" Victoria 3 Event Gui window"""

	def __init__(self):
		self.char_1_tab = GuiWindows["char_1_tab"]
		self.char_1_lord = GuiWindows["char_1_lord"]
		self.char_1_propaganda = GuiWindows["char_1_propaganda"]
		self.char_2 = GuiWindows["char_2"]
		self.big_icon = GuiWindows["big_icon"]


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
	"book": "gfx/interface/icons/event_icons/tutorial_icon.dds",
	"academics": "gfx/event_icons/academics.dds",
	"active_peace_deal": "gfx/event_icons/active_peace_deal.dds",
	"aristocrats": "gfx/event_icons/aristocrats.dds",
	"fabric_roll": "gfx/event_icons/fabric_roll.dds",
	"gemstone": "gfx/event_icons/gemstone.dds",
	"armillary": "gfx/event_icons/armillary.dds",
	"bell": "gfx/event_icons/bell.dds",
	"bureaucrats": "gfx/event_icons/bureaucrats.dds",
	"capitalists": "gfx/event_icons/capitalists.dds",
	"character_busy": "gfx/event_icons/character_busy.dds",
	"clergymen": "gfx/event_icons/clergymen.dds",
	"clerks": "gfx/event_icons/clerks.dds",
	"diplomatic_play": "gfx/event_icons/diplomatic_play.dds",
	"economic_dominance": "gfx/event_icons/economic_dominance.dds",
	"egalitarian_society": "gfx/event_icons/egalitarian_society.dds",
	"engineers": "gfx/event_icons/engineers.dds",
	"farmers": "gfx/event_icons/farmers.dds",
	"force_recognition": "gfx/event_icons/force_recognition.dds",
	"has_no_research": "gfx/event_icons/has_no_research.dds",
	"hegemon": "gfx/event_icons/hegemon.dds",
	"icon_kill": "gfx/event_icons/icon_kill.dds",
	"laborers": "gfx/event_icons/laborers.dds",
	"legitimacy": "gfx/event_icons/legitimacy.dds",
	"literacy": "gfx/event_icons/literacy.dds",
	"machinists": "gfx/event_icons/machinists.dds",
	"market_isolated": "gfx/event_icons/market_isolated.dds",
	"officers": "gfx/event_icons/officers.dds",
	"peasants": "gfx/event_icons/peasants.dds",
	"power_projection": "gfx/event_icons/power_projection.dds",
	"raid_convoys": "gfx/event_icons/raid_convoys.dds",
	"shopkeepers": "gfx/event_icons/shopkeepers.dds",
	"slaves": "gfx/event_icons/slaves.dds",
	"soldiers": "gfx/event_icons/soldiers.dds",
	"standby": "gfx/event_icons/standby.dds",
	"supply_low": "gfx/event_icons/supply_low.dds",
	"take_colony": "gfx/event_icons/take_colony.dds",
	"take_treaty_port": "gfx/event_icons/take_treaty_port.dds",
	"tutorial_icon": "gfx/event_icons/tutorial_icon.dds",
	"unit_attack": "gfx/event_icons/unit_attack.dds",
	"unit_defense": "gfx/event_icons/unit_defense.dds",
	"war_reparations": "gfx/event_icons/war_reparations.dds",
	"wasted_construction": "gfx/event_icons/wasted_construction.dds",
	"academia": "gfx/event_icons/academia.dds",
	"aeroplanes": "gfx/event_icons/aeroplanes.dds",
	"analytical_philosophy": "gfx/event_icons/analytical_philosophy.dds",
	"anarchy": "gfx/event_icons/anarchy.dds",
	"army_reserves": "gfx/event_icons/army_reserves.dds",
	"automobiles": "gfx/event_icons/automobiles.dds",
	"banking": "gfx/event_icons/banking.dds",
	"bureaucracy": "gfx/event_icons/bureaucracy.dds",
	"canneries": "gfx/event_icons/canneries.dds",
	"central_archives": "gfx/event_icons/central_archives.dds",
	"combustion_engine": "gfx/event_icons/combustion_engine.dds",
	"compression_ignition": "gfx/event_icons/compression_ignition.dds",
	"currency_standards": "gfx/event_icons/currency_standards.dds",
	"democracy": "gfx/event_icons/democracy.dds",
	"enlistment_offices": "gfx/event_icons/enlistment_offices.dds",
	"film": "gfx/event_icons/film.dds",
	"fine_art": "gfx/event_icons/fine_art.dds",
	"food": "gfx/event_icons/food.dds",
	"human_rights": "gfx/event_icons/human_rights.dds",
	"hydraulic_cranes": "gfx/event_icons/hydraulic_cranes.dds",
	"international_diplomacy": "gfx/event_icons/international_diplomacy.dds",
	"international_exchange_standards": "gfx/event_icons/international_exchange_standards.dds",
	"international_trade": "gfx/event_icons/international_trade.dds",
	"labor_movement": "gfx/event_icons/labor_movement.dds",
	"lathe": "gfx/event_icons/lathe.dds",
	"law_enforcement": "gfx/event_icons/law_enforcement.dds",
	"lightbulbs": "gfx/event_icons/lightbulbs.dds",
	"line_infantry": "gfx/event_icons/line_infantry.dds",
	"literature": "gfx/event_icons/literature.dds",
	"locomotives": "gfx/event_icons/locomotives.dds",
	"macroeconomics": "gfx/event_icons/macroeconomics.dds",
	"manufacturies": "gfx/event_icons/manufacturies.dds",
	"mass_propaganda": "gfx/event_icons/mass_propaganda.dds",
	"mass_surveillance": "gfx/event_icons/mass_surveillance.dds",
	"mechanized_farming": "gfx/event_icons/mechanized_farming.dds",
	"military_aviation": "gfx/event_icons/military_aviation.dds",
	"military_statistics": "gfx/event_icons/military_statistics.dds",
	"nationalism": "gfx/event_icons/nationalism.dds",
	"navigation": "gfx/event_icons/navigation.dds",
	"paddle_steamer": "gfx/event_icons/paddle_steamer.dds",
	"pan_nationalism": "gfx/event_icons/pan_nationalism.dds",
	"paper": "gfx/event_icons/paper.dds",
	"philosophical_pragmatism": "gfx/event_icons/philosophical_pragmatism.dds",
	"political_agitation": "gfx/event_icons/political_agitation.dds",
	"postal_savings": "gfx/event_icons/postal_savings.dds",
	"power_of_the_purse": "gfx/event_icons/power_of_the_purse.dds",
	"prospecting_tech": "gfx/event_icons/prospecting_tech.dds",
	"psychoanalysis": "gfx/event_icons/psychoanalysis.dds",
	"pumpjacks": "gfx/event_icons/pumpjacks.dds",
	"radio": "gfx/event_icons/radio.dds",
	"railways": "gfx/event_icons/railways.dds",
	"rationalism": "gfx/event_icons/rationalism.dds",
	"realism": "gfx/event_icons/realism.dds",
	"sea_lane_strategies": "gfx/event_icons/sea_lane_strategies.dds",
	"shift_work": "gfx/event_icons/shift_work.dds",
	"socialism": "gfx/event_icons/socialism.dds",
	"standing_army": "gfx/event_icons/standing_army.dds",
	"steam_donkey": "gfx/event_icons/steam_donkey.dds",
	"steelworking": "gfx/event_icons/steelworking.dds",
	"stock_exchanges": "gfx/event_icons/stock_exchanges.dds",
	"tools": "gfx/event_icons/tools.dds",
	"urbanization": "gfx/event_icons/urbanization.dds",
	"zeppelins": "gfx/event_icons/zeppelins.dds",
	"clippers": "gfx/event_icons/clippers.dds",
	"drydock": "gfx/event_icons/drydock.dds",
	"electrical_capacitors": "gfx/event_icons/electrical_capacitors.dds",
	"electrical_generation": "gfx/event_icons/electrical_generation.dds",
	"ironclads": "gfx/event_icons/ironclads.dds",
	"man_o_wars": "gfx/event_icons/man_o_wars.dds",
	"oil": "gfx/event_icons/oil.dds",
	"opium": "gfx/event_icons/opium.dds",
	"paddle_steamer": "gfx/event_icons/paddle_steamer.dds",
	"porcelain": "gfx/event_icons/porcelain.dds",
	"psychiatry": "gfx/event_icons/psychiatry.dds",
	"rubber": "gfx/event_icons/rubber.dds",
	"screw_frigate": "gfx/event_icons/screw_frigate.dds",
	"shaft_mining": "gfx/event_icons/shaft_mining.dds",
	"shell_gun": "gfx/event_icons/shell_gun.dds",
	"steamers": "gfx/event_icons/steamers.dds",
	"steel_railway_cars": "gfx/event_icons/steel_railway_cars.dds",
	"telephones": "gfx/event_icons/telephones.dds",
	"transportation": "gfx/event_icons/transportation.dds",
	"war_propaganda": "gfx/event_icons/war_propaganda.dds",
	"wargaming": "gfx/event_icons/wargaming.dds",
	"watertube_boiler": "gfx/event_icons/watertube_boiler.dds",
	"wine": "gfx/event_icons/wine.dds",
	"ammunition": "gfx/event_icons/ammunition.dds",
	"artillery": "gfx/event_icons/artillery.dds",
	"breech_loading_artillery": "gfx/event_icons/breech_loading_artillery.dds",
	"dreadnought": "gfx/event_icons/dreadnought.dds",
	"military_drill": "gfx/event_icons/military_drill.dds",
	"destroyers": "gfx/event_icons/destroyers.dds",
	"mobile_armor": "gfx/event_icons/mobile_armor.dds",
	"monitor_tech": "gfx/event_icons/monitor_tech.dds",
	"luxury_clothes": "gfx/event_icons/luxury_clothes.dds",
}


EventSounds = {
	"industry": "event:/SFX/Events/europenorthamerica/london_center",
	"ironclad": "event:/SFX/Events/unspecific/steam_ship",
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
	"ironclad": "event_image = {\n\t\ttexture = \"gfx/event_pictures/paintings/harbors/The_Paying_out_Machinery_in_the_Stern_of_the_Great_Eastern.dds\"\n\t}",
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
	"char_1_tab": "event_window_1char_tabloid",
	"char_1_lord": "event_window_1char_lord_kitchener",
	"char_1_propaganda": "event_window_1char_propaganda",
	"char_2": "event_window_2char",
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
			OR = {
				religion = rel:sunni
				religion = rel:shiite
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
	event_image = {
		# Default
		trigger = {
			NOR = {
				OR = {
					religion = rel:sunni
					religion = rel:shiite
				}
				ruler.culture = {
					OR = {
						has_culture_graphics = african
						has_culture_graphics = asian
						has_culture_graphics = european
						has_culture_graphics = mideast_indian
					}
				}
			}
		}
		video = "gfx/event_pictures/unspecific_politicians_arguing.bk2"
	}
''')

city = Template('''pdx
event_image = { trigger = { var:picture = 1 } texture = "gfx/event_pictures/paintings/cities/An_Overshot_Mill_in_Wales_James_Ward.dds" }
	event_image = { trigger = { var:picture = 2 } texture = "gfx/event_pictures/paintings/cities/Cole_Thomas_View_of_Florence_from_San_Miniato_1837.dds" }
	event_image = { trigger = { var:picture = 3 } texture = "gfx/event_pictures/paintings/cities/The_945_Accommodation.dds" }
	event_image = { trigger = { var:picture = 4 } texture = "gfx/event_pictures/paintings/cities/Thomas_Malton_the_Younger_High_Street_Oxford.dds" }
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
			OR = {
				religion = rel:sunni
				religion = rel:shiite
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
	event_image = {
		trigger = {
			ruler.culture = { has_culture_graphics = african } 
		}
		video = "gfx/event_pictures/africa_public_protest.bk2"
	}
	event_image = { trigger = { ruler.culture = { has_culture_graphics = asian } } video = "gfx/event_pictures/asia_union_leader.bk2" }
	event_image = { trigger = { ruler.culture = { has_culture_graphics = european } } video = "gfx/event_pictures/europenorthamerica_springtime_of_nations.bk2" }
	event_image = { trigger = { ruler.culture = { has_culture_graphics = mideast_indian } } video = "gfx/event_pictures/asia_sepoy_mutiny.bk2" }
	event_image = {
		# Default
		trigger = {
			NOR = {
				OR = {
					religion = rel:sunni
					religion = rel:shiite
				}
				ruler.culture = {
					OR = {
						has_culture_graphics = african
						has_culture_graphics = asian
						has_culture_graphics = european
						has_culture_graphics = mideast_indian
					}
				}
			}
		}
		video = "gfx/event_pictures/unspecific_vandalized_storefront.bk2"
	}
''')

industry = Template('''pdx
event_image = {
		trigger = {
			OR = {
				religion = rel:sunni
				religion = rel:shiite
			}
		}
		video = "gfx/event_pictures/middleeast_engineer_blueprint.bk2"
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
		video = "gfx/event_pictures/southamerica_factory_opening.bk2"
	}
	event_image = { trigger = { ruler.culture = { has_culture_graphics = african } } video = "gfx/event_pictures/africa_construction_colony.bk2" }
	event_image = { trigger = { ruler.culture = { has_culture_graphics = asian } } video = "gfx/event_pictures/asia_farmers_market.bk2" }
	event_image = { trigger = { ruler.culture = { has_culture_graphics = european } } video = "gfx/event_pictures/europenorthamerica_london_center.bk2" }
	event_image = { trigger = { ruler.culture = { has_culture_graphics = mideast_indian } } video = "gfx/event_pictures/asia_farmers_market.bk2" }
	event_image = {
		# Default
		trigger = {
			NOR = {
				OR = {
					religion = rel:sunni
					religion = rel:shiite
				}
				ruler.culture = {
					OR = {
						has_culture_graphics = african
						has_culture_graphics = asian
						has_culture_graphics = european
						has_culture_graphics = mideast_indian
					}
				}
			}
		}
		video = "gfx/event_pictures/unspecific_gears_pistons.bk2"
	}
''')

religion = Template('''pdx
event_image = {
		trigger = {
			religion = rel:jewish
		}
		video = "gfx/event_pictures/europenorthamerica_judaism.bk2"
	}
	event_image = {
		trigger = {
			OR = {
				religion = rel:protestant
				religion = rel:catholic
				religion = rel:orthodox
				religion = rel:oriental_orthodox
			}
		}
		video = "gfx/event_pictures/southamerica_christianity.bk2"
	}
	event_image = {
		trigger = {
			OR = {
				religion = rel:hindu
				religion = rel:sikh
			}
		}
		video = "gfx/event_pictures/asia_hinduism_sikhism.bk2"
	}
	event_image = {
		trigger = {
			religion = rel:shinto
		}
		video = "gfx/event_pictures/asia_confucianism_shinto.bk2"
	}
	event_image = {
		trigger = {
			ruler.culture = {
				has_discrimination_trait = indigenous_american_heritage
			}
		}
		video = "gfx/event_pictures/europenorthamerica_native_american.bk2"
	}
	event_image = {
		trigger = {
			OR = {
				religion = rel:mahayana
				religion = rel:gelugpa
				religion = rel:theravada
			}
		}
		video = "gfx/event_pictures/asia_buddhism.bk2"
	}
	event_image = {
		trigger = {
			OR = {
				religion = rel:sunni
				religion = rel:shiite
			}
		}
		video = "gfx/event_pictures/middleeast_islam.bk2"
	}
	event_image = {
		trigger = {
			NOR = {
				religion = rel:jewish
				religion = rel:protestant
				religion = rel:catholic
				religion = rel:orthodox
				religion = rel:oriental_orthodox
				religion = rel:mahayana
				religion = rel:gelugpa
				religion = rel:theravada
				religion = rel:shinto
				religion = rel:hindu
				religion = rel:sikh
				religion = rel:sunni
				religion = rel:shiite
				ruler.culture = {
					has_discrimination_trait = indigenous_american_heritage
				}
			}
		}
		video = "gfx/event_pictures/africa_animism.bk2"
	}
''')
