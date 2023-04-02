from jinja2 import Template
from event import Event, EventFile
from data import EventImage, Sound, Icon, GuiWindow

namespace = "MFE_trade_good_events"
video = EventImage()
sound = Sound()
icon = Icon()
gui = GuiWindow()

ev1 = Event(
	header="Bullets for [SCOPE.sW('active_war').GetName]",
	namespace=namespace,
	eventid="1",
	placement="scope:munitions_state",
	minor_left_icon="g:ammunition",
	minor_right_icon="g:ammunition",
	icon=icon.ammunition,
	cooldown="long",
	trigger=Template('''pdx
	trigger = {
		any_scope_war = {
			count > 0
		}
		any_scope_building = {
			has_ammo_pm = yes
			is_building_type = building_munition_plants
			average_building_trigger = yes
			level >= 5
		}
	}
	''').render()[3:],
	immediate=Template('''pdx
	immediate = {
		random_scope_war = {
			save_scope_as = active_war
		}
		random_scope_building = {
			limit = {
				has_ammo_pm = yes
				is_building_type = building_munition_plants
				average_building_trigger = yes
				level >= 5
			}
			save_scope_as = munitions_building
			state = {
				save_scope_as = munitions_state
			}
		}
	}
	''').render()[3:],
	option=Template('''pdx
	option = {
		name = {{namespace}}.1.a
		default_option = yes
		# Just in time for the war
		scope:munitions_building = {
			add_modifier = {
				name = MFE_lots_of_bullets_mod
				months = normal_modifier_time
			}
		}
	}
	''').render(namespace=namespace)[3:],
)

ev2 = Event(
	header="[SCOPE.sC('ally').GetName] is short on bullets for [SCOPE.sW('active_war').GetName]",
	namespace=namespace,
	eventid="2",
	minor_left_icon="ruler",
	placement="scope:ammo_state",
	minor_right_icon="scope:ally.ruler",
	icon=icon.ammunition,
	event_image=video.diplo,
	on_opened_soundeffect=sound.get("diplo"),
	cooldown="long",
	trigger=Template('''pdx
	trigger = {
		ally_in_war_short_on_goods_trigger = {
			goods = "ammunition"
		}
		market.mg:ammunition = {
			market_goods_has_goods_shortage = no
		}
		any_scope_building = {
			has_ammo_pm = yes
			is_building_type = building_munition_plants
			rich_building_trigger = yes
			level >= 5
		}
	}
	''').render()[3:],
	immediate=Template('''pdx
	immediate = {
		ally_in_war_short_on_goods_effect = {
			goods = "ammunition"
		}
		random_scope_building = {
			limit = {
				has_ammo_pm = yes
				is_building_type = building_munition_plants
				rich_building_trigger = yes
				level >= 5
			}
			save_scope_as = ammo_building
			state = { save_scope_as = ammo_state }
		}
		scope:ally = {
			random_scope_building = {
				limit = {
					has_ammo_pm = yes
					is_building_type = building_munition_plants
				}
				save_scope_as = ally_ammo_building
				state = { save_scope_as = ally_ammo_state }
			}
		}
	}
	''').render()[3:],
	option=Template('''pdx
	option = {
		name = {{namespace}}.2.a
		default_option = yes
		# We can spare a few bullets
		set_obligation = {
			actor = scope:ally
			target = root
		}
		scope:ammo_building = {
			add_modifier = {
				name = MFE_sending_ally_bullets_mod
				months = normal_modifier_time
			}
		}
		scope:ally_ammo_building = {
			add_modifier = {
				name = MFE_ally_sent_bullets_mod
				months = normal_modifier_time
			}
		}
		scope:ally = {
			create_trade_route = {
				goods = ammunition
				level = 1
				direction = import
				target = root.market
			}
			#create_trade_route = {
			#	goods = ammunition
			#	level = 1
			#	import = yes
			#	origin = scope:ammo_state.state_region
			#	target = scope:ally_ammo_state.state_region
			#}
		}
	}
	''').render(namespace=namespace)[3:],
	option2=Template('''pdx
	option = {
		name = {{namespace}}.2.b
		# How are we going to shoot our enemies without bullets?!
		scope:ally = {
			change_relations = {
				country = root
				value = -25
			}
		}
	}
	''').render(namespace=namespace)[3:],
)

ev3 = Event(
	header="[SCOPE.sC('ally').GetName] is short on artillery for [SCOPE.sW('active_war').GetName]",
	namespace=namespace,
	eventid="3",
	placement="scope:artillery_state",
	minor_left_icon="ruler",
	minor_right_icon="scope:ally.ruler",
	icon=icon.shell_gun,
	gui_window=gui.big_icon,
	event_image=video.diplo,
	on_opened_soundeffect=sound.get("diplo"),
	cooldown="long",
	trigger=Template('''pdx
	trigger = {
		ally_in_war_short_on_goods_trigger = {
			goods = "artillery"
		}
		market.mg:artillery = {
			market_goods_has_goods_shortage = no
		}
		any_scope_building = {
			has_artillery_pm = yes
			is_building_type = building_arms_industry
			rich_building_trigger = yes
			level >= 5
		}
	}
	''').render()[3:],
	immediate=Template('''pdx
	immediate = {
		ally_in_war_short_on_goods_effect = {
			goods = "artillery"
		}
		random_scope_building = {
			limit = {
				has_artillery_pm = yes
				is_building_type = building_arms_industry
				rich_building_trigger = yes
				level >= 5
			}
			save_scope_as = artillery_building
			state = {
				save_scope_as = artillery_state
			}
		}
		scope:ally = {
			random_scope_building = {
				limit = {
					has_artillery_pm = yes
					is_building_type = building_arms_industry
				}
				save_scope_as = ally_artillery_building
				state = { save_scope_as = ally_artillery_state }
			}
		}
	}
	''').render()[3:],
	option=Template('''pdx
	option = {
		name = {{namespace}}.3.a
		default_option = yes
		# We can spare a few artillery pieces
		set_obligation = {
			actor = scope:ally
			target = root
		}
		scope:artillery_building = {
			add_modifier = {
				name = MFE_sending_ally_artillery_mod
				months = normal_modifier_time
			}
		}
		scope:ally_artillery_building = {
			add_modifier = {
				name = MFE_ally_sent_artillery_mod
				months = normal_modifier_time
			}
		}
		scope:ally = {
			create_trade_route = {
				goods = artillery
				level = 1
				direction = import
				target = root.market
			}
		}
	}
	''').render(namespace=namespace)[3:],
	option2=Template('''pdx
	option = {
		name = {{namespace}}.3.b
		# How will we blow up our enemies without artillery?!
		scope:ally = {
			change_relations = {
				country = root
				value = -25
			}
		}
	}
	''').render(namespace=namespace)[3:],
)

ev4 = Event(
	header="Materials for Artillery Shells dissapear from the factory in [SCOPE.sS('arms_state').GetName]",
	namespace=namespace,
	eventid="4",
	placement="scope:artillery_state",
	icon=icon.artillery,
	event_image=video.get("unspecific_vandalized_storefront"),
	on_opened_soundeffect=sound.get("unspecific_vandalized_storefront"),
	cooldown="very_long",
	trigger=Template('''pdx
	trigger = {
		market.mg:artillery = {
			market_goods_has_goods_shortage = no
		}
		any_scope_building = {
			has_artillery_pm = yes
			is_building_type = building_arms_industry
			average_building_trigger = yes
			level >= 5
		}
	}
	''').render()[3:],
	immediate=Template('''pdx
	immediate = {
		random_scope_building = {
			limit = {
				has_artillery_pm = yes
				is_building_type = building_arms_industry
				average_building_trigger = yes
				level >= 5
			}
			state = {
				save_scope_as = artillery_state
			}
		}
	}
	''').render()[3:],
	option=Template('''pdx
	option = {
		name = {{namespace}}.4.a
		default_option = yes
		# Hopefully they did not fall into the wrong hands...
		scope:artillery_state = {
			add_modifier = {
				name = MFE_artillery_stolen_from_state_mod
				months = normal_modifier_time
			}
		}
	}
	''').render(namespace=namespace)[3:],
)

ev5 = Event(
	header="Farms in [SCOPE.sS('arable_state').GetName] having a great season",
	namespace=namespace,
	eventid="5",
	placement="scope:arable_state",
	icon=icon.peasants,
	gui_window=gui.big_icon,
	event_image=video.landscape,
	on_opened_soundeffect=sound.get("landscape"),
	cooldown="long",
	trigger=Template('''pdx
	trigger = {
		has_food_shortage = yes
		any_scope_building = {
			state = {
				arable_land > 100
			}
			rich_building_trigger = yes
			level >= 10
		}
	}
	''').render()[3:],
	immediate=Template('''pdx
	immediate = {
		get_landscape_picture = yes
		random_scope_building = {
			limit = {
				state = {
					arable_land > 75
				}
				is_farm = yes
				rich_building_trigger = yes
				level >= 10
			}
			state = {
				save_scope_as = arable_state
			}
		}
	}
	''').render()[3:],
	option=Template('''pdx
	option = {
		name = {{namespace}}.5.a
		default_option = yes
		# There couldn't have been a better time
		scope:arable_state = {
			ordered_scope_building = {
				limit = {
					is_farm = yes
				}
				order_by = level
				max = 3
				add_modifier = {
					name = MFE_propering_farms_mod
					months = normal_modifier_time
				}
			}
		}
	}
	''').render(namespace=namespace)[3:],
)

ev6 = Event(
	header="Madman at the Tank Factory in [SCOPE.sS('tank_state').GetName]",
	namespace=namespace,
	eventid="6",
	placement="scope:tank_state",
	icon=icon.mobile_armor,
	minor_left_icon="g:tanks",
	minor_right_icon="g:tanks",
	event_image=video.get("unspecific_devastation"),
	on_opened_soundeffect=sound.get("unspecific_destruction"),
	cooldown="very_long",
	trigger=Template('''pdx
	trigger = {
		any_scope_building = {
			is_building_type = building_war_machine_industry
			has_active_production_method = pm_tank_production
			occupancy >= 0.5
			level >= 1
			level < 7
		}
	}
	''').render()[3:],
	immediate=Template('''pdx
	immediate = {
		random_scope_building = {
			limit = {
				is_building_type = building_war_machine_industry
				has_active_production_method = pm_tank_production
				occupancy >= 0.5
				level >= 1
				level < 7
			}
			state = {
				save_scope_as = tank_state
			}
		}
		scope:tank_state = {
			remove_building = building_war_machine_industry
		}
	}
	''').render()[3:],
	option=Template('''pdx
	option = {
		name = {{namespace}}.6.a
		default_option = yes
		# Hopefully they get over it
		scope:tank_state = {
			add_modifier = {
				name = MFE_tank_factory_destruction_mod
				duration = normal_modifier_time
			}
		}
	}
	''').render(namespace=namespace)[3:],
	option2=Template('''pdx
	option = {
		name = {{namespace}}.6.b
		# Give them anything they need this is just awful...
		scope:tank_state = {
			add_modifier = {
				name = MFE_tank_factory_destruction_aid_sent_mod
				duration = normal_modifier_time
			}
		}
		add_modifier = {
			name = MFE_sent_tank_destruction_aid_mod
			days = 365
		}
	}
	''').render(namespace=namespace)[3:],
)

ev7 = Event(
	header="Private Planes bring Rich Investors in [SCOPE.sS('plane_state').GetName]",
	namespace=namespace,
	eventid="7",
	placement="scope:plane_state",
	icon=icon.aeroplanes,
	event_image=video.get("unspecific_airplane"),
	on_opened_soundeffect=sound.get("unspecific_airplane"),
	cooldown="long",
	trigger=Template('''pdx
	trigger = {
		any_scope_building = {
			has_active_production_method = pm_aeroplane_production
			rich_building_trigger = yes
			level >= 3
		}
	}
	''').render()[3:],
	immediate=Template('''pdx
	immediate = {
		random_scope_building = {
			limit = {
				has_active_production_method = pm_aeroplane_production
				rich_building_trigger = yes
				level >= 3
			}
			state = {
				save_scope_as = plane_state
			}
		}
	}
	''').render()[3:],
	option=Template('''pdx
	option = {
		name = {{namespace}}.7.a
		default_option = yes
		# It's a great time to live in [SCOPE.GetRootScope.GetCountry.GetName]
		scope:plane_state = {
			add_modifier = {
				name = MFE_plane_investors_state_mod
				duration = normal_modifier_time
			}
		}
	}
	''').render(namespace=namespace)[3:],
)

ev8 = Event(
	header="Poor quality iron in the boats of [SCOPE.sS('ironclad_state').GetName]",
	namespace=namespace,
	eventid="8",
	placement="scope:ironclad_state",
	icon=icon.scales,
	event_image=video.ironclad,
	gui_window=gui.big_icon,
	on_opened_soundeffect=sound.ironclad,
	cooldown="long",
	trigger=Template('''pdx
	trigger = {
		any_scope_building = {
			has_ironclad_pm = yes
			poor_building_trigger = yes
		}
	}
	''').render()[3:],
	immediate=Template('''pdx
	immediate = {
		get_harbor_picture = yes
		random_scope_building = {
			limit = {
				has_ironclad_pm = yes
				poor_building_trigger = yes
			}
			save_scope_as = ironclad_building
			state = {
				save_scope_as = ironclad_state
			}
		}
	}
	''').render()[3:],
	option=Template('''pdx
	option = {
		name = {{namespace}}.8.a
		default_option = yes
		# Hopefully the iron gets better
		scope:ironclad_building = {
			add_modifier = {
				name = MFE_ironclad_badiron_mod
				duration = normal_modifier_time
			}
		}
	}
	''').render(namespace=namespace)[3:],
)

ev9 = Event(
	header="Grain shortage in [SCOPE.sS('grain_state').GetName] is causing trouble",
	namespace=namespace,
	eventid="9",
	placement="scope:grain_state",
	icon=icon.trade,
	event_image=video.get("unspecific_vandalized_storefront"),
	on_opened_soundeffect=sound.get("unspecific_vandalized_storefront"),
	cooldown="long",
	trigger=Template('''pdx
	trigger = {
		any_scope_building = {
			has_grain_pm = yes
			cash_reserves_ratio > 0.25
			weekly_profit < 1
			occupancy >= 0.1
			level >= 4
		}
	}
	''').render()[3:],
	immediate=Template('''pdx
	immediate = {
		random_scope_building = {
			limit = {
				has_grain_pm = yes
				cash_reserves_ratio > 0.25
				weekly_profit < 1
				occupancy >= 0.1
				level >= 4
			}
			state = {
				save_scope_as = grain_state
			}
		}
	}
	''').render()[3:],
	option=Template('''pdx
	option = {
		name = {{namespace}}.9.a
		default_option = yes
		# Do they really need food to live?
		scope:grain_state = {
			add_modifier = {
				name = MFE_starving_state_mod
				duration = normal_modifier_time
			}
		}
	}
	option = {
		name = {{namespace}}.9.b
		# Redirect some funds to [SCOPE.sS('grain_state').GetName]
		scope:grain_state = {
			add_modifier = {
				name = MFE_starving_state_aid_sent_mod
				duration = normal_modifier_time
			}
		}
		add_modifier = {
			name = MFE_aiding_starving_state_mod
			duration = normal_modifier_time
		}
	}
	option = {
		name = {{namespace}}.9.c
		# Last I checked there was plenty of cake to eat in the shops of [SCOPE.sS('grain_state').GetName]
		trigger = {
			ruler = {
				OR = {
					has_trait = wrathful
					has_trait = cruel
				}
			}
		}
		scope:grain_state = {
			add_modifier = {
				name = MFE_low_food_cake_mod
				duration = normal_modifier_time
			}
		}
	}
	''').render(namespace=namespace)[3:],
)

ev10 = Event(
	header="The fish in [SCOPE.sS('fish_state').GetName] is far too fishy",
	namespace=namespace,
	eventid="10",
	placement="scope:fish_state",
	icon=icon.human_rights,
	minor_left_icon="g:fish",
	minor_right_icon="g:fish",
	event_image=video.harbors,
	gui_window=gui.big_icon,
	on_opened_soundeffect=sound.harbors,
	cooldown="very_long",
	trigger=Template('''pdx
	trigger = {
		any_scope_building = {
			is_building_type = building_fishing_wharf
			level >= 4
		}
	}
	''').render()[3:],
	immediate=Template('''pdx
	immediate = {
		get_harbor_picture = yes
		random_scope_building = {
			limit = {
				is_building_type = building_fishing_wharf
				level >= 4
			}
			save_scope_as = fish_building
			state = {
				save_scope_as = fish_state
			}
		}
	}
	''').render()[3:],
	option=Template('''pdx
	option = {
		name = {{namespace}}.10.a
		default_option = yes
		# How can fish be too fishy?
		scope:fish_building = {
			add_modifier = {
				name = MFE_very_fishy_fish_mod
				duration = long_modifier_time
			}
		}
	}
	''').render(namespace=namespace)[3:],
)

ev11 = Event(
	header="Man O Wars in [SCOPE.sS('ship_state').GetName] are ready for war",
	namespace=namespace,
	eventid="11",
	placement="scope:ship_state",
	icon=icon.man_o_wars,
	event_image=video.get("unspecific_vandalized_storefront"),
	on_opened_soundeffect=sound.get("unspecific_vandalized_storefront"),
	cooldown="very_long",
	trigger=Template('''pdx
	trigger = {
		is_at_war = no
		any_scope_building = {
			has_manowar_pm = yes
			level >= 3
		}
	}
	''').render()[3:],
	immediate=Template('''pdx
	immediate = {
		random_scope_building = {
			limit = {
				has_manowar_pm = yes
				level >= 3
			}
			state = {
				save_scope_as = ship_state
			}
		}
	}
	''').render()[3:],
)

ev12 = Event(
	header="Fine fabrics of [SCOPE.sS('fabric_state').GetName]",
	namespace=namespace,
	eventid="12",
	placement="scope:fabric_state",
	icon=icon.economic_dominance,
	event_image=video.landscape,
	gui_window=gui.big_icon,
	on_opened_soundeffect=sound.get("landscape"),
	cooldown="long",
	trigger=Template('''pdx
	trigger = {
		any_scope_building = {
			has_good_fabric_pm = yes
			level >= 7
		}
	}
	''').render()[3:],
	immediate=Template('''pdx
	immediate = {
		get_landscape_picture = yes
		random_scope_building = {
			limit = {
				has_good_fabric_pm = yes
				level >= 7
			}
			state = {
				save_scope_as = fabric_state
			}
		}
	}
	''').render()[3:],
)

ev13 = Event(
	header="Fire in the sawmills of [SCOPE.sS('sawmill_fire_state').GetName]",
	namespace=namespace,
	eventid="13",
	placement="scope:sawmill_fire_state",
	icon=icon.fire,
	event_image=video.get("unspecific_fire"),
	on_opened_soundeffect=sound.get("unspecific_fire"),
	cooldown="very_long",
	trigger=Template('''pdx
	trigger = {
		any_scope_building = {
			has_active_production_method = pm_saw_mills
			level >= 5
		}
	}
	''').render()[3:],
	immediate=Template('''pdx
	immediate = {
		random_scope_building = {
			limit = {
				has_active_production_method = pm_saw_mills
				level >= 5
			}
			state = {
				save_scope_as = sawmill_fire_state
			}
		}
	}
	''').render()[3:],
)

ev14 = Event(
	header="Hardwood in [SCOPE.sS('hardwood_state').GetName] is extremely hard",
	namespace=namespace,
	eventid="14",
	placement="scope:hardwood_state",
	icon=icon.unit_attack,
	event_image=video.get("europenorthamerica_gold_prospectors"),
	on_opened_soundeffect=sound.get("europenorthamerica_gold_prospectors"),
	cooldown="very_long",
	trigger=Template('''pdx
	trigger = {
		any_scope_building = {
			has_active_production_method = pm_hardwood
			level >= 5
		}
	}
	''').render()[3:],
	immediate=Template('''pdx
	immediate = {
		random_scope_building = {
			limit = {
				has_active_production_method = pm_hardwood
				level >= 5
			}
			state = {
				save_scope_as = hardwood_state
			}
		}
	}
	''').render()[3:],
)

ev15 = Event(
	header="Entire Grocery chain robbed in grand organized crime in [SCOPE.sS('grocery_state').GetName]",
	namespace=namespace,
	eventid="15",
	placement="scope:grocery_state",
	icon=icon.supply_low,
	event_image=video.get("unspecific_vandalized_storefront"),
	on_opened_soundeffect=sound.get("unspecific_vandalized_storefront"),
	cooldown="very_long",
	trigger=Template('''pdx
	trigger = {
		market_capital.market.mg:groceries = { 
			market_goods_pricier > 0.25
		}
		any_scope_building = {
			has_groceries_pm = yes
			poor_building_trigger = yes
			level >= 5
		}
	}
	''').render()[3:],
	immediate=Template('''pdx
	immediate = {
		random_scope_building = {
			limit = {
				has_groceries_pm = yes
				poor_building_trigger = yes
				level >= 5
			}
			state = {
				save_scope_as = grocery_state
			}
		}
	}
	''').render()[3:],
)

ev16 = Event(
	header="People in [SCOPE.sS('clothes_state').GetName] can't afford to wear clothes",
	namespace=namespace,
	eventid="16",
	placement="scope:clothes_state",
	icon=icon.anarchy,
	event_image=video.europenorthamerica_rich_and_poor,
	on_opened_soundeffect=sound.europenorthamerica_rich_and_poor,
	cooldown="very_long",
	trigger=Template('''pdx
	trigger = {
		market_capital.market.mg:clothes = { 
			market_goods_pricier > 0.25
			market_goods_has_goods_shortage = yes
			market_goods_shortage_ratio < 0.15
		}
		any_scope_building = {
			has_clothes_pm = yes
			poor_building_trigger = yes
			level >= 2
		}
	}
	''').render()[3:],
	immediate=Template('''pdx
	immediate = {
		random_scope_building = {
			limit = {
				has_clothes_pm = yes
				poor_building_trigger = yes
				level >= 2
			}
			state = {
				save_scope_as = clothes_state
			}
		}
	}
	''').render()[3:],
)

ev17 = Event(
	header="[SCOPE.GetRootScope.GetCountry.GetRuler.GetFullName] dies after sitting on chair while visiting the furniture factory in [SCOPE.sS('furniture_state').GetName]",
	namespace=namespace,
	eventid="17",
	placement="scope:furniture_state",
	icon=icon.skull,
	event_image=video.unspecific_factory_closed,
	on_opened_soundeffect=sound.unspecific_factory_closed,
	cooldown="very_long",
	weight_multiplier=Template('''pdx
	weight_multiplier = {
		base = -1
		modifier = {
			factor = -100
			ruler = {
				has_trait = cautious
			}
		}
		modifier = {
			factor = 2
			ruler = {
				has_trait = reckless
			}
		}
	}
	''').render()[3:],
	trigger=Template('''pdx
	trigger = {
		capital = {
			exists = b:building_furniture_manufacturies
			b:building_furniture_manufacturies = {
				poor_building_trigger = yes
				level >= 1
			}
		}
	}
	''').render()[3:],
	immediate=Template('''pdx
	immediate = {
		capital = {
			save_scope_as = furniture_state
		}
	}
	''').render()[3:],
)

ev18 = Event(
	header="Extreme production of paper in [SCOPE.sS('paper_state').GetName] awes the world",
	namespace=namespace,
	eventid="18",
	placement="scope:paper_state",
	icon=icon.literature,
	event_image=video.southamerica_factory_opening,
	on_opened_soundeffect=sound.southamerica_factory_opening,
	trigger=Template('''pdx
	trigger = {
		NOT = { has_variable = paper_world_event_happened }
		any_scope_building = {
			is_building_type = building_paper_mills
			level >= 30
		}
	}
	''').render()[3:],
	immediate=Template('''pdx
	immediate = {
		set_variable = paper_world_event_happened
		random_scope_building = {
			limit = {
				is_building_type = building_paper_mills
				level >= 30
			}
			save_scope_as = huge_paper_factory
			state = {
				save_scope_as = paper_state
			}
		}
	}
	''').render()[3:],
)

ev19 = Event(
	header="The disappearing stars of [SCOPE.sS('power_state').GetName]",
	namespace=namespace,
	eventid="19",
	placement="scope:power_state",
	icon=icon.lightbulbs,
	event_image=video.city,
	on_opened_soundeffect=sound.city,
	gui_window=gui.big_icon,
	trigger=Template('''pdx
	trigger = {
		NOT = { has_variable = electricity_stars_event_happened }
		any_scope_building = {
			is_building_type = building_power_plant
			level >= 5
		}
	}
	''').render()[3:],
	immediate=Template('''pdx
	immediate = {
		get_city_picture = yes
		set_variable = electricity_stars_event_happened
		random_scope_building = {
			limit = {
				is_building_type = building_power_plant
				level >= 5
			}
			save_scope_as = power_plant
			state = {
				save_scope_as = power_state
			}
		}
	}
	''').render()[3:],
)

ev20 = Event(
	header="Huge explosion in sulfur mines in [SCOPE.sS('sulfur_state').GetName] destroys the mine and kills workers",
	namespace=namespace,
	eventid="20",
	placement="scope:sulfur_state",
	icon=icon.raid_convoys,
	event_image=video.industry,
	on_opened_soundeffect=sound.industry,
	cooldown="very_long",
	trigger=Template('''pdx
	trigger = {
		any_scope_building = {
			is_building_type = building_sulfur_mine
			mine_is_using_explosives = yes
			level >= 2
			level < 10
		}
	}
	''').render()[3:],
	immediate=Template('''pdx
	immediate = {
		random_scope_building = {
			limit = {
				is_building_type = building_sulfur_mine
				mine_is_using_explosives = yes
				level >= 2
				level < 10
			}
			state = {
				save_scope_as = sulfur_state
				remove_building = building_sulfur_mine
			}
		}
	}
	''').render()[3:],
)

ev21 = Event(
	header="Huge explosion in lead mines in [SCOPE.sS('lead_state').GetName] destroys the mine and kills workers",
	namespace=namespace,
	eventid="21",
	placement="scope:lead_state",
	icon=icon.skull,
	event_image=video.industry,
	on_opened_soundeffect=sound.industry,
	cooldown="very_long",
	trigger=Template('''pdx
	trigger = {
		any_scope_building = {
			is_building_type = building_lead_mine
			mine_is_using_explosives = yes
			level >= 2
			level < 8
		}
	}
	''').render()[3:],
	immediate=Template('''pdx
	immediate = {
		random_scope_building = {
			limit = {
				is_building_type = building_lead_mine
				mine_is_using_explosives = yes
				level >= 2
				level < 8
			}
			state = {
				save_scope_as = lead_state
				remove_building = building_sulfur_mine
			}
		}
	}
	''').render()[3:],
)

ev22 = Event(
	header="Lead from the mines in [SCOPE.sS('lead_state').GetName] has shown up in the water",
	namespace=namespace,
	eventid="22",
	placement="scope:lead_state",
	icon=icon.icon_kill,
	gui_window=gui.big_icon,
	event_image=video.landscape,
	on_opened_soundeffect=sound.landscape,
	cooldown="very_long",
	trigger=Template('''pdx
	trigger = {
		any_scope_building = {
			is_building_type = building_lead_mine
			level >= 8
		}
	}
	''').render()[3:],
	immediate=Template('''pdx
	immediate = {
		get_landscape_picture = yes
		random_scope_building = {
			limit = {
				is_building_type = building_lead_mine
				level >= 8
			}
			state = {
				save_scope_as = lead_state
			}
		}
	}
''').render()[3:],
)

ev23 = Event(
	header="The beginning of a new age...led by rubber",
	namespace=namespace,
	eventid="23",
	placement="scope:rubber_state",
	icon=icon.rubber,
	gui_window=gui.big_icon,
	event_image=video.landscape,
	minor_left_icon="g:rubber",
	minor_right_icon="g:rubber",
	on_opened_soundeffect=sound.landscape,
	trigger=Template('''pdx
	trigger = {
		NOT = { has_variable = rubber_boom_started_var }
		year < 1870
		any_scope_building = {
			is_building_type = building_rubber_plantation
			level >= 3
		}
	}
	''').render()[3:],
	immediate=Template('''pdx
	immediate = {
		get_landscape_picture = yes
		set_variable = rubber_boom_started_var
		random_scope_building = {
			limit = {
				is_building_type = building_rubber_plantation
				level >= 3
			}
			state = {
				save_scope_as = rubber_state
			}
		}
	}
	''').render()[3:],
)

ev24 = Event(
	header="Black Gold of [SCOPE.sS('oil_state').GetName]",
	namespace=namespace,
	eventid="24",
	placement="scope:oil_state",
	icon=icon.oil,
	event_image=video.middleeast_oil_derricks,
	minor_left_icon="g:oil",
	minor_right_icon="g:oil",
	on_opened_soundeffect=sound.middleeast_oil_derricks,
	cooldown="very_long",
	trigger=Template('''pdx
	trigger = {
		any_scope_building = {
			is_building_type = building_oil_rig
			level >= 5
		}
	}
	''').render()[3:],
	immediate=Template('''pdx
	immediate = {
		random_scope_building = {
			limit = {
				is_building_type = building_oil_rig
				level >= 5
			}
			state = {
				save_scope_as = oil_state
			}
		}
	}
	''').render()[3:],
)

ev25 = Event(
	header="Steel Factory Destroying communities of [SCOPE.sS('steel_state').GetName]",
	namespace=namespace,
	eventid="25",
	placement="scope:steel_state",
	icon=icon.manufacturies,
	event_image=video.industry,
	on_opened_soundeffect=sound.industry,
	cooldown="very_long",
	trigger=Template('''pdx
	trigger = {
		any_scope_building = {
			rich_building_trigger = yes
			is_building_type = building_steel_mills
			level >= 5
		}
	}
	''').render()[3:],
	immediate=Template('''pdx
	immediate = {
		random_scope_building = {
			limit = {
				rich_building_trigger = yes
				is_building_type = building_steel_mills
				level >= 5
			}
			state = {
				save_scope_as = steel_state
			}
		}
	}
	''').render()[3:],
)

if __name__ == '__main__':
	MFE_trade_goods = EventFile(
		namespace, ev1.event, ev2.event, ev3.event, ev4.event,
		ev5.event, ev6.event, ev7.event, ev8.event, ev9.event,
		ev10.event, ev11.event, ev12.event, ev13.event, ev14.event,
		ev15.event, ev16.event, ev17.event, ev18.event, ev19.event,
		ev20.event, ev21.event, ev22.event, ev23.event, ev24.event, ev25.event)

	# events = [ev1, ev2, ev3, ev4, ev5, ev6, ev7, ev8, ev9, ev10, ev11, ev12, ev13, ev14, ev15, ev16, ev17, ev18, ev19, ev20, ev21, ev22, ev23, ev24, ev25]
	# for i in events:
	# 	print(i.header)
