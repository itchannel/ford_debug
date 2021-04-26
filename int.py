value = {} 
value["value"] = "Fully_Closed2"
window_closed_status = ["Fully_Closed", "Fully_closed_position", "Undefined_window_position"];


if value["value"] not in window_closed_status:
	print("open")
