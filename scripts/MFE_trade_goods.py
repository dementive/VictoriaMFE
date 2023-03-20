from jinja2 import Template
from event import Video, GuiWindows, Event, EventFile

textures = """pdx
	video = "gfx/event_pictures/africa_diplomats_negotiating.bk2"
	icon = "gfx/interface/icons/event_icons/event_military.dds"
	on_opened_soundeffect = "event:/SFX/Events/unspecific/vandalized_storefront"
"""
video = Video()

def ally_in_war_short_on_goods_trigger(goods):
	temp=Template('''pdx
		any_scope_war = {
			count > 0
		}
		any_scope_ally = {
			root = {
				is_in_war_together = prev
				NOT = {
					has_war_with = prev
				}
			}
			market.mg:{{goods}} = {
				market_goods_has_goods_shortage = yes
			}
		}
	''').render(goods=goods)[6:]
	return temp

def ally_in_war_short_on_goods_effect(goods):
	temp=Template('''pdx
		random_scope_war = {
			save_scope_as = active_war
		}
		random_scope_ally = {
			limit = {
				root = {
					is_in_war_together = prev
					NOT = {
						has_war_with = prev
					}
				}
				market.mg:{{goods}} = {
					market_goods_has_goods_shortage = yes
				}
			}
			save_scope_as = ally
		}
	''').render(goods=goods)[6:]
	return temp

namespace = "MFE_trade_good_events"

# Bullets for [active_war.GetName]
ev1 = Event(
namespace=namespace,
eventid="1",
placement="scope:munitions_state",
minor_left_icon="g:ammunition",
minor_right_icon="g:ammunition",
icon="gfx/interface/icons/event_icons/event_military.dds",
trigger=Template('''pdx
	trigger = {
		any_scope_war = {
			count > 0
		}
		any_scope_building = {
			has_ammo_pm = yes
			is_building_type = building_munition_plants
			cash_reserves_ratio > 0.25
			weekly_profit > 0
			occupancy >= 0.5
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
				cash_reserves_ratio > 0.25
				weekly_profit > 0
				occupancy >= 0.5
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

# [ally.GetName] is short on bullets for [active_war.GetName]
ev2 = Event(
namespace=namespace,
eventid="2",
minor_left_icon="ruler",
placement="scope:ammo_state",
minor_right_icon="scope:ally.ruler",
icon="gfx/interface/icons/event_icons/event_military.dds",
event_image=video.diplo,
trigger=Template('''pdx
	trigger = {
		{{trigger}}
    	market.mg:ammunition = {
    		market_goods_has_goods_shortage = no
    	}
    	any_scope_building = {
    		has_ammo_pm = yes
			is_building_type = building_munition_plants
			cash_reserves_ratio > 0.25
			weekly_profit > 0
			occupancy >= 0.5
			level >= 5
    	}
	}
''').render(trigger=ally_in_war_short_on_goods_trigger(goods="ammunition"))[3:],
immediate=Template('''pdx
	immediate = {
		{{effect}}
		random_scope_building = {
			limit = {
				has_ammo_pm = yes
				is_building_type = building_munition_plants
				cash_reserves_ratio > 0.25
				weekly_profit > 0
				occupancy >= 0.5
				level >= 5
			}
			save_scope_as = ammo_state
		}
	}
''').render(effect=ally_in_war_short_on_goods_effect(goods="ammunition"))[3:],
)

# [ally.GetName] is short on artillery for [active_war.GetName]
ev3 = Event(
namespace=namespace,
eventid="3",
placement="scope:artillery_state",
minor_left_icon="ruler",
minor_right_icon="scope:ally.ruler",
icon="gfx/interface/icons/event_icons/event_military.dds",
event_image=video.diplo,
trigger=Template('''pdx
	trigger = {
		{{trigger}}
    	market.mg:artillery = {
    		market_goods_has_goods_shortage = no
    	}
    	any_scope_building = {
    		has_artillery_pm = yes
			is_building_type = building_arms_industry
			cash_reserves_ratio > 0.25
			weekly_profit > 0
			occupancy >= 0.5
			level >= 5
    	}
	}
	''').render(trigger=ally_in_war_short_on_goods_trigger(goods="artillery"))[3:],
immediate=Template('''pdx
	immediate = {
		{{effect}}
		random_scope_building = {
			limit = {
				has_artillery_pm = yes
				is_building_type = building_arms_industry
				cash_reserves_ratio > 0.25
				weekly_profit > 0
				occupancy >= 0.5
				level >= 5
			}
			state = {
				save_scope_as = artillery_state
			}
		}
	}
''').render(effect=ally_in_war_short_on_goods_effect(goods="artillery"))[3:],
)

# Materials for Artillery Shells dissapear from the factory in [arms_state.GetName]...
ev4 = Event(
namespace=namespace,
eventid="4",
placement="scope:artillery_state",
icon="gfx/interface/icons/event_icons/event_military.dds",
event_image=video.get("unspecific_vandalized_storefront"),
on_opened_soundeffect="event:/SFX/Events/unspecific/vandalized_storefront",
trigger=Template('''pdx
	trigger = {
    	market.mg:artillery = {
    		market_goods_has_goods_shortage = no
    	}
    	any_scope_building = {
    		has_artillery_pm = yes
			is_building_type = building_arms_industry
			cash_reserves_ratio > 0.25
			weekly_profit > 0
			occupancy >= 0.5
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
				cash_reserves_ratio > 0.25
				weekly_profit > 0
				occupancy >= 0.5
				level >= 5
			}
			state = {
				save_scope_as = artillery_state
			}
		}
	}
''').render()[3:],
)


# Farms in [arable_state] having a great season
ev5 = Event(
namespace=namespace,
eventid="5",
placement="scope:arable_state",
icon="gfx/interface/icons/event_icons/event_military.dds",
event_image=video.landscape,
on_opened_soundeffect="event:/SFX/Events/europenorthamerica/gold_prospectors",
trigger=Template('''pdx
	trigger = {
		any_scope_building = {
			state = {
				arable_land > 100
			}
			cash_reserves_ratio > 0.25
			weekly_profit > 0
			occupancy >= 0.5
			level >= 5
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
				cash_reserves_ratio > 0.25
				weekly_profit > 0
				occupancy >= 0.5
				level >= 5
			}
			state = {
				save_scope_as = arable_state
			}
		}
	}
''').render()[3:],
)

if __name__ == '__main__':
	MFE_trade_goods = EventFile(namespace, ev1.event, ev2.event, ev3.event, ev4.event, ev5.event)
