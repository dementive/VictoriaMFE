from jinja2 import Template
from event import Event, EventFile
import data

namespace = "MFE_trade_good_events"
textures = """pdx
	video = "gfx/event_pictures/africa_diplomats_negotiating.bk2"
	icon = "gfx/interface/icons/event_icons/event_military.dds"
	on_opened_soundeffect = "event:/SFX/Events/unspecific/vandalized_storefront"
"""
video = data.Video()
sound = data.Sound()

ev1 = Event(
	header="Bullets for [active_war.GetName]",
	namespace=namespace,
	eventid="1",
	placement="scope:munitions_state",
	minor_left_icon="g:ammunition",
	minor_right_icon="g:ammunition",
	icon="gfx/interface/icons/event_icons/event_military.dds",
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
)

ev2 = Event(
	header="[ally.GetName] is short on bullets for [active_war.GetName]",
	namespace=namespace,
	eventid="2",
	minor_left_icon="ruler",
	placement="scope:ammo_state",
	minor_right_icon="scope:ally.ruler",
	icon="gfx/interface/icons/event_icons/event_military.dds",
	gui_window=data.GuiWindows["big_icon"],
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
			save_scope_as = ammo_state
		}
	}
''').render()[3:],
)

ev3 = Event(
	header="[ally.GetName] is short on artillery for [active_war.GetName]",
	namespace=namespace,
	eventid="3",
	placement="scope:artillery_state",
	minor_left_icon="ruler",
	minor_right_icon="scope:ally.ruler",
	icon="gfx/interface/icons/event_icons/event_military.dds",
	gui_window=data.GuiWindows["big_icon"],
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
			state = {
				save_scope_as = artillery_state
			}
		}
	}
''').render()[3:],
)

ev4 = Event(
	header="Materials for Artillery Shells dissapear from the factory in [arms_state.GetName]...",
	namespace=namespace,
	eventid="4",
	placement="scope:artillery_state",
	icon="gfx/interface/icons/event_icons/event_military.dds",
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
)

ev5 = Event(
	header="Farms in [arable_state] having a great season",
	namespace=namespace,
	eventid="5",
	placement="scope:arable_state",
	icon="gfx/interface/icons/event_icons/event_military.dds",
	gui_window=data.GuiWindows["big_icon"],
	event_image=video.landscape,
	on_opened_soundeffect=sound.get("landscape"),
	cooldown="long",
	trigger=Template('''pdx
	trigger = {
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
					arable_land > 100
				}
				rich_building_trigger = yes
				level >= 10
			}
			state = {
				save_scope_as = arable_state
			}
		}
	}
''').render()[3:],
)

ev6 = Event(
	header="Madman at the Tank Factory in [tank_state.GetName]",
	namespace=namespace,
	eventid="6",
	placement="scope:tank_state",
	icon="gfx/interface/icons/event_icons/event_fire.dds",
	minor_left_icon="g:tanks",
	minor_right_icon="g:tanks",
	event_image=video.get("unspecific_devastation"),
	on_opened_soundeffect=sound.get("unspecific_destruction"),
	cooldown="long",
	trigger=Template('''pdx
	trigger = {
		any_scope_building = {
			has_active_production_method = pm_tank_production
			occupancy >= 0.5
			level >= 5
		}
	}
	''').render()[3:],
	immediate=Template('''pdx
	immediate = {
		random_scope_building = {
			limit = {
				has_active_production_method = pm_tank_production
				occupancy >= 0.5
				level >= 5
			}
			state = {
				save_scope_as = tank_state
			}
		}
	}
''').render()[3:],
)

ev7 = Event(
	header="Private Planes bring Rich Investors in [plane_state.GetName]",
	namespace=namespace,
	eventid="7",
	placement="scope:plane_state",
	icon="gfx/interface/icons/event_icons/event_trade.dds",
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
)

ev8 = Event(
	header="Poor quality iron in the boats of [ironclad_state.GetName]",
	namespace=namespace,
	eventid="8",
	placement="scope:ironclad_state",
	icon="gfx/interface/icons/event_icons/event_trade.dds",
	event_image=video.get("unspecific_factory_closed"),
	on_opened_soundeffect=sound.get("unspecific_factory_closed"),
	cooldown="long",
	trigger=Template('''pdx
	trigger = {
		any_scope_building = {
			has_ironclad_pm = yes
			poor_building_trigger = yes
			level >= 3
		}
	}
	''').render()[3:],
	immediate=Template('''pdx
	immediate = {
		random_scope_building = {
			limit = {
				has_ironclad_pm = yes
				poor_building_trigger = yes
				level >= 3
			}
			state = {
				save_scope_as = ironclad_state
			}
		}
	}
''').render()[3:],
)

ev9 = Event(
	header="Grain shortage in [grain_state.GetName] is causing trouble",
	namespace=namespace,
	eventid="9",
	placement="scope:ironclad_state",
	icon="gfx/interface/icons/event_icons/event_trade.dds",
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
)

ev10 = Event(
	header="The fish in [fish_state.GetName] is far too fishy",
	namespace=namespace,
	eventid="10",
	placement="scope:fish_state",
	icon="gfx/interface/icons/event_icons/event_skull.dds",
	minor_left_icon="g:fish",
	minor_right_icon="g:fish",
	event_image=video.get("unspecific_whaling"),
	on_opened_soundeffect=sound.get("unspecific_whaling"),
	cooldown="very_long",
	trigger=Template('''pdx
	trigger = {
		any_scope_building = {
			this = b:building_fishing_wharf
			level >= 4
		}
	}
	''').render()[3:],
	immediate=Template('''pdx
	immediate = {
		random_scope_building = {
			limit = {
				this = b:building_fishing_wharf
				level >= 4
			}
			state = {
				save_scope_as = fish_state
			}
		}
	}
''').render()[3:],
)

ev11 = Event(
	header="Man O Wars in [ship_state.GetName] are ready for war",
	namespace=namespace,
	eventid="11",
	placement="scope:ship_state",
	icon="gfx/interface/icons/event_icons/event_trade.dds",
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
	header="Fine fabrics of [fabric_state.GetName]",
	namespace=namespace,
	eventid="12",
	placement="scope:fabric_state",
	icon="gfx/interface/icons/event_icons/event_trade.dds",
	event_image=video.landscape,
	gui_window="big_icon",
	on_opened_soundeffect=sound.get("landscape"),
	cooldown="long",
	trigger=Template('''pdx
	trigger = {

		is_at_war = no
		any_scope_building = {
			has_good_fabric_pm = yes
			level >= 3
		}
	}
	''').render()[3:],
	immediate=Template('''pdx
	immediate = {
		random_scope_building = {
			limit = {
				has_good_fabric_pm = yes
				level >= 3
			}
			state = {
				save_scope_as = fabric_state
			}
		}
	}
''').render()[3:],
)

if __name__ == '__main__':
	MFE_trade_goods = EventFile(
		namespace, ev1.event, ev2.event, ev3.event, ev4.event,
		ev5.event, ev6.event, ev7.event, ev8.event, ev9.event,
		ev10.event, ev11.event, ev12.event)
