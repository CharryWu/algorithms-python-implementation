extends KinematicBody2D

var rotate_time = 0.8

var detector_area_1 = false
var detector_area_2 = false
var detector_area_3 = false
var detector_area_4 = false

func _ready():
	get_node("TouchArea2D").connect("input_event",self,"_on_Area2D_input_event")

func _on_Area2D_input_event( viewport, event, shape_idx ):
	if Input.is_action_just_released("click"):
		rotate_block()

func rotate_block():
	var rotate_to = rotation_degrees+90
	if fmod(rotate_to,90) != 0:	
		rotate_to += 90 - fmod(rotate_to,90)
	var tween = create_tween()
	tween.tween_property(self,"rotation_degrees", rotate_to, rotate_time)

func _on_DetectorArea2D1_area_entered(area):
	if area.name != "TouchArea2D":
		detector_area_1 = true
	detector_area_entered()

func _on_DetectorArea2D1_area_exited(area):
	if area.name != "TouchArea2D":
		detector_area_1 = false
	detector_area_entered()

func _on_DetectorArea2D2_area_entered(area):
	if area.name != "TouchArea2D":
		detector_area_2 = true
	detector_area_entered()

func _on_DetectorArea2D2_area_exited(area):
	if area.name != "TouchArea2D":
		detector_area_2 = false
	detector_area_entered()

func _on_DetectorArea2D3_area_entered(area):
	if area.name != "TouchArea2D":
		detector_area_3 = true
	detector_area_entered()


func _on_DetectorArea2D3_area_exited(area):
	if area.name != "TouchArea2D":
		detector_area_3 = false
	detector_area_entered()


func _on_DetectorArea2D4_area_entered(area):
	if area.name != "TouchArea2D":
		detector_area_4 = true
	detector_area_entered()


func _on_DetectorArea2D4_area_exited(area):
	if area.name != "TouchArea2D":
		detector_area_4 = false
	detector_area_entered()

func detector_area_entered():
	if detector_area_1 and detector_area_2 and detector_area_3 and detector_area_4:
		modulate = Color(0.5, 0, 0, 1)
	else:
		modulate = Color(1, 1, 1, 1)
