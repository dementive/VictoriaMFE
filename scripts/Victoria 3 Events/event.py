import codecs
from jinja2 import Template

event = Template('''pdx{% if blank is not defined %}{% set blank = "" %}{% endif %}{% if header != blank %}\n\n# {{header}}{% endif %}
{{namespace}}.{{eventid}} = {
	{% if eventtype != blank %}type = {{eventtype}}{% else %}type = country_event{% endif %}
	{% if placement != blank %}placement = {{placement}}{% else %}placement = root{% endif %}
	{% if title != blank %}title = {{title}}{% else %}title = "{{namespace}}.{{eventid}}.t"{% endif %}
	{% if desc != blank %}desc = {{desc}}{% else %}desc = "{{namespace}}.{{eventid}}.d"{% endif %}
	{% if flavor != blank %}flavor = {{flavor}}{% else %}flavor = "{{namespace}}.{{eventid}}.f"{% endif %}
	{% if duration != blank %}duration = {{duration}}
	{% else %}duration = 3{% endif %}
	{% if icon != blank %}icon = "{{icon}}"
	{% else %}icon = "gfx/interface/icons/event_icons/event_military.dds"{% endif %}
	{% if right_icon != blank %}right_icon = {{right_icon}}\n\t{% endif %}{% if minor_left_icon != blank %}minor_left_icon = {{minor_left_icon}}\n\t{% endif %}{% if minor_right_icon != blank %}minor_right_icon = {{minor_right_icon}}\n\t{% endif %}{% if center_icon != blank %}center_icon = {{center_icon}}\n\t{% endif %}{% if gui_window != blank %}gui_window = {{gui_window}}\n\t{% endif %}{% if left_icon != blank %}left_icon = {{left_icon}}\n\t{% endif %}{% if event_image != blank %}{{event_image}}
	{% else %}
	event_image = {
		video = "gfx/event_pictures/unspecific_gears_pistons.bk2"
	}
	{% endif %}
	{% if on_created_soundeffect != blank %}on_created_soundeffect = "{{on_created_soundeffect}}"
	{% else %}on_created_soundeffect = "event:/SFX/UI/Alerts/event_appear"{% endif %}
	{% if on_opened_soundeffect != blank %}on_opened_soundeffect = "{{on_opened_soundeffect}}"
	{% else %}on_opened_soundeffect = "event:/SFX/Events/unspecific/gears_pistons"{% endif %}{{weight_multiplier}}{% if cooldown != blank %}\n\tcooldown = { months = {{cooldown}}_cooldown }{% endif %}{% if cancellation_trigger != blank %}\n\t{{cancellation_trigger}}{% endif %}{% if trigger != blank %}{{trigger}}{% else %}\n\ttrigger = {\n\n\t}{% endif %}{% if immediate != blank %}{{immediate}}{% else %}
	immediate = {

	}{% endif %}{% if option != blank %}{{option}}
	{% else %}
	option = {
		name = {{namespace}}.{{eventid}}.a
		default_option = yes
	}{% endif %}{% if option2 != blank %}{{option2}}
	{% else %}
	option = {
		name = {{namespace}}.{{eventid}}.b
	}{% endif %}{% if after != blank %}\n\t{{after}}{% endif %}
}
''')


class Event():
	"""Victoria 3 event"""

	def __init__(self,
		header="",
		namespace="",
		eventid="",
		eventtype="",
		placement="",
		title="",
		desc="",
		flavor="",
		duration="",
		event_image="",
		gui_window="",
		left_icon="",
		right_icon="",
		center_icon="",
		minor_left_icon="",
		minor_right_icon="",
		icon="",
		weight_multiplier="",
		on_created_soundeffect="",
		on_opened_soundeffect="",
		cooldown="",
		cancellation_trigger="",
		trigger="",
		immediate="",
		option="",
		option2="",
		after=""):

		self.header = header
		self.event = event.render(
			header=header,
			namespace=namespace,
			eventid=eventid,
			eventtype=eventtype,
			placement=placement,
			title=title,
			desc=desc,
			flavor=flavor,
			duration=duration,
			event_image=event_image,
			gui_window=gui_window,
			left_icon=left_icon,
			right_icon=right_icon,
			center_icon=center_icon,
			minor_left_icon=minor_left_icon,
			minor_right_icon=minor_right_icon,
			icon=icon,
			weight_multiplier=weight_multiplier,
			on_created_soundeffect=on_created_soundeffect,
			on_opened_soundeffect=on_opened_soundeffect,
			trigger=trigger,
			cooldown=cooldown,
			cancellation_trigger=cancellation_trigger,
			immediate=immediate,
			option=option,
			option2=option2,
			after=after
		)[4:]


class EventFile():
	""" Victoria 3 event file"""

	def __init__(self, *args):
		self.file = ""
		self.namespace = args[0]
		self.make_file(args)

	def make_file(self, args):
		for i, j in enumerate(args):
			if i == 0: j = f"# Generated file, dont change manually or changes will be lost.\n\nnamespace = {self.namespace}"
			self.file += j + "\n"
		self.write()

	def write(self, add_bom=True):
		path = f"events\\{self.namespace}.txt"
		with open(path, "w") as file:
			file.write(self.file)
		if add_bom:
			EventFile.add_utf8_bom(path)

	@staticmethod
	def add_utf8_bom(filename):
		with codecs.open(filename, 'r', 'utf-8') as f:
			content = f.read()
		with codecs.open(filename, 'w', 'utf-8') as f2:
			f2.write('\ufeff')
			f2.write(content)
		return
