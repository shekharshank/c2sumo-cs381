import sys
sys.path.insert(0, '/app/Middleware')

from DBUtil import *
db = DBUtil().getDatabase()

mapLocation = "/app/Map/"

def createTrafficData(problem6c = False):
    state = [
        "Green!0g!1!2-Red!3!4-Red!5g!6-Red!7!8-Green!9g!10!11-Red!12!13-Red!14g!15-Red!16!17",
    	"Yellow!0g!1!2-Red!3!4-Red!5g!6-Red!7!8-Yellow!9g!10!11-Red!12!13-Red!14g!15-Red!16!17",
    	"Red!0g!1!2-Green!3!4-Red!5g!6-Red!7!8-Red!9g!10!11-Green!12!13-Red!14g!15-Red!16!17",
    	"Red!0g!1!2-Yellow!3!4-Red!5g!6-Red!7!8-Red!9g!10!11-Yellow!12!13-Red!14g!15-Red!16!17",
    	"Red!0g!1!2-Red!3!4-Green!5g!6-Red!7!8-Red!9g!10!11-Red!12!13-Green!14g!15-Red!16!17",
    	"Red!0g!1!2-Red!3!4-Yellow!5g!6-Red!7!8-Red!9g!10!11-Red!12!13-Yellow!14g!15-Red!16!17",
    	"Red!0g!1!2-Red!3!4-Red!5g!6-Green!7!8-Red!9g!10!11-Red!12!13-Red!14g!15-Green!16!17",
    	"Red!0g!1!2-Red!3!4-Red!5g!6-Yellow!7!8-Red!9g!10!11-Red!12!13-Red!14g!15-Yellow!16!17"
    ]

    duration_green = 10
    duration_yellow = 2

    dataList = []
    # only return the first 4 states if this is problem 6c
    endVal = 4 if problem6c else 8
    for i in range(0, endVal):

        trafficLightLogic = {
            "state": state[i],
            # alternate between duration_green and duration_yellow
            "duration": duration_green if i % 2 == 0 else duration_yellow
        }
        dataList.append(trafficLightLogic)
    return dataList

def initTrafficProblems(problemArea):
    junction1 = {
        "_id": "202305472",
        "traffic_data": createTrafficData(),
        "turn_probability": {
            "19485812#3": {
        		"left_turn": "0.2",
        		"right_turn": "0.2",
        		"go_straight": "0.6",
        		"to_edge_left": "-19457616#3",
        		"to_edge_right": "19457616#4",
        		"to_edge_straight": "-19456179#4"
            },
            "19457616#3": {
        		"left_turn": "0.2",
        		"right_turn": "0.2",
        		"go_straight": "0.6",
        		"to_edge_left": "-19456179#4",
        		"to_edge_right": "-19485812#3",
        		"to_edge_straight": "19457616#4"
            },
            "19456179#4": {
        		"left_turn": "0.2",
        		"right_turn": "0.2",
        		"go_straight": "0.6",
        		"to_edge_left": "19457616#4",
        		"to_edge_right": "-19457616#3",
        		"to_edge_straight": "-19485812#3"
            },
            "-19457616#4": {
        		"left_turn": "0.2",
        		"right_turn": "0.2",
        		"go_straight": "0.6",
        		"to_edge_left": "-19485812#3",
        		"to_edge_right": "-19456179#4",
        		"to_edge_straight": "-19457616#3"
            }
        },

        "flow_data": [
        	#		| B					| C
        	#		| 					|
        	#		| 		Iwest		|
        	# --A-- O1-----------------	O2---D---
        	#		|		Ieast		|
        	#		|					|
        	# Lsouth| Lnorth	Jsouth	| Jnorth
        	#		|					|
        	#		|		Keast		|
        	# --H-- O4----------------- O3---E---
        	#		|		Kwest		|
        	#		|					|
        	#		| G					| F
            {"point_name": "A",
    		"from_edge_id": "19485812#3",
    		"to_edge_id": "n/a",
    		"via_edge_id": "19485812#3",
    	    "flow_rate": "600",
    		"latitude":"36.13950836759643",
    		"longitude": "-86.8132084608078",
    		"removable": "0"},
            {"point_name": "B",
    		"from_edge_id": "19457616#3",
    		"to_edge_id": "n/a",
    		"via_edge_id": "19457616#3",
    	    "flow_rate": "600",
    		"latitude": "36.13948079754408",
    		"longitude": "-86.81078642606735",
    		"removable": "0"},
            {"point_name": "Iwest",
    		"from_edge_id": "19456179#4",
    		"to_edge_id": "n/a",
    		"via_edge_id": "19456179#4",
    	    "flow_rate": "600",
    		"latitude": "36.138289149356346",
    		"longitude": "-86.80801838636398",
    		"removable": "0"},
            {"point_name": "Ieast",
    		"from_edge_id": "-19456179#0",
    		"to_edge_id": "n/a",
    		"via_edge_id": "-19456179#0",
    	    "flow_rate": "600",
    		"latitude": "36.138387177653954",
    		"longitude": "-86.80800765752792",
    		"removable": "1"},
            {"point_name": "Lnorth",
    		"from_edge_id": "-19457616#4",
    		"to_edge_id": "n/a",
    		"via_edge_id": "-19457616#4",
    	    "flow_rate": "600",
    		"latitude": "36.13720010799972",
    		"longitude": "-86.81105330586433",
    		"removable": "0"},
            {"point_name": "Lsouth",
    		"from_edge_id": "-19457616#4",
    		"to_edge_id": "n/a",
    		"via_edge_id": "-19457616#4",
    	    "flow_rate": "600",
    		"latitude": "36.137777562190905",
    		"longitude": "-86.81101977825165",
    		"removable": "1"}
        ],
        "west_lane_out":"-19485812#3",
	    "west_lane_out_values":["-19485812#3_0","-19485812#3_1"],
	    "west_lane_in":"19485812#3",
	    "west_lane_in_values":["19485812#3_1", "19485812#3_0"],
	    # left, straight, right
	    "west_lane_in_adjascent":["-19457616#3", "-19456179#4", "19457616#4"],

	    "east_lane_in":"19456179#4",
	    "east_lane_in_values":["19456179#4_0","19456179#4_1"],
	    "east_lane_in_adjascent":["19457616#4", "-19485812#3", "-19457616#3"],
	    "east_lane_out":"-19456179#4",
	    "east_lane_out_values":["-19456179#4_1", "-19456179#4_0"],

	    "north_lane_in":"19457616#3",
	    "north_lane_in_values":["19457616#3_0","19457616#3_1"],
	    "north_lane_in_adjascent":["-19456179#4", "19457616#4", "-19485812#3"],
	    "north_lane_out":"-19457616#3",
	    "north_lane_out_values":["-19457616#3_1","-19457616#3_0"],

	    "south_lane_out":"19457616#4",
	    "south_lane_out_values":["19457616#4_0","19457616#4_1"],
	    "south_lane_in":"-19457616#4",
	    "south_lane_in_values":["-19457616#4_1", "-19457616#4_0"],
	    "south_lane_in_adjascent":["-19485812#3", "-19457616#3", "-19456179#4"],
        "induction_loop": {
            "-19485812#3_0_5" : {
                "location": "west_lane_out",
        	    "pos": 5
            },
            "-19485812#3_1_5": {
                "location": "west_lane_out",
        	    "pos": 5
            },
            "19485812#3_0_-5": {
                "location": "west_lane_in",
        	    "pos": -5
            },
            "19485812#3_1_-5": {
                "location": "west_lane_in",
        	    "pos": -5
            },
            "-19456179#4_0_5": {
                "location": "east_lane_out",
        	    "pos": 5
            },
            "-19456179#4_1_5": {
                "location": "east_lane_out",
        	    "pos": 5
            },
            "19456179#4_0_-5": {
                "location": "east_lane_in",
        	    "pos": -5
            },
            "19456179#4_1_-5": {
                "location": "east_lane_in",
        	    "pos": -5
            },
            "-19457616#3_0_5": {
                "location": "north_lane_out",
        	    "pos": 5
            },
            "-19457616#3_1_5": {
                "location": "north_lane_out",
        	    "pos": 5
            },
            "19457616#3_0_-5": {
                "location": "north_lane_in",
        	    "pos": -5
            },
            "19457616#3_1_-5": {
                "location": "north_lane_in",
        	    "pos": -5
            },
            "19457616#4_0_5": {
                "location": "south_lane_out",
        	    "pos": 5
            },
            "19457616#4_1_5": {
                "location": "south_lane_out",
        	    "pos": 5
            },
            "-19457616#4_0_-5": {
                "location": "south_lane_in",
        	    "pos": -5
            },
            "-19457616#4_1_-5": {
                "location": "south_lane_in",
        	    "pos": -5
            }
        }
    }

    junction2 = {
        "_id": "202305458",
        "traffic_data": createTrafficData(),
        "turn_probability": {
            "-19456179#0": {
        		"left_turn": "0.3",
        		"right_turn": "0.3",
        		"go_straight": "0.4",
        		"to_edge_left": "-19463160#7",
        		"to_edge_right": "19463160#8",
        		"to_edge_straight": "-19479801#4"
            },
            "19463160#7": {
        		"left_turn": "0.3",
        		"right_turn": "0.3",
        		"go_straight": "0.4",
        		"to_edge_left": "-19479801#4",
        		"to_edge_right": "19456179#0",
        		"to_edge_straight": "19463160#8"
            },
            "19479801#4": {
        		"left_turn": "0.3",
        		"right_turn": "0.3",
        		"go_straight": "0.4",
        		"to_edge_left": "19463160#8",
        		"to_edge_right": "-19463160#7",
        		"to_edge_straight": "19456179#0"
            },
            "-19463160#8": {
        		"left_turn": "0.3",
        		"right_turn": "0.3",
        		"go_straight": "0.4",
        		"to_edge_left": "19456179#0",
        		"to_edge_right": "-19479801#4",
        		"to_edge_straight": "-19463160#7"
            }
        },
        "flow_data": [
            #		| B					| C
        	#		| 					|
        	#		| 		Iwest		|
        	# --A-- O1-----------------	O2---D---
        	#		|		Ieast		|
        	#		|					|
        	# Lsouth| Lnorth	Jsouth	| Jnorth
        	#		|					|
        	#		|		Keast		|
        	# --H-- O4----------------- O3---E---
        	#		|		Kwest		|
        	#		|					|
        	#		| G					| F
            {"point_name": "C",
			"from_edge_id": "19463160#7",
			"to_edge_id": "n/a",
			"via_edge_id": "19463160#7",
		    "flow_rate": "600",
			"latitude":"36.138488",
			"longitude": "-86.800700",
			"removable": "0"},
            {"point_name": "D",
    		"from_edge_id": "19479801#4",
    		"to_edge_id": "n/a",
    		"via_edge_id": "19479801#4",
    	    "flow_rate": "600",
    		"latitude": "36.137566",
    		"longitude": "-86.799433",
    		"removable": "0"},
            {"point_name": "Iwest",
    		"from_edge_id": "19456179#4",
    		"to_edge_id": "n/a",
    		"via_edge_id": "19456179#4",
    	    "flow_rate": "600",
    		"latitude": "36.138289149356346",
    		"longitude": "-86.80801838636398",
    		"removable": "1"},
            {"point_name": "Ieast",
    		"from_edge_id": "-19456179#0",
    		"to_edge_id": "n/a",
    		"via_edge_id": "-19456179#0",
    	    "flow_rate": "600",
    		"latitude": "36.138387177653954",
    		"longitude": "-86.80800765752792",
    		"removable": "0"},
            {"point_name": "Jnorth",
    		"from_edge_id": "-19463160#8",
    		"to_edge_id": "n/a",
    		"via_edge_id": "-19463160#8",
    	    "flow_rate": "600",
    		"latitude": "36.13587822736727",
    		"longitude": "-86.80091857910156",
    		"removable": "0"},
            {"point_name": "Jsouth",
    		"from_edge_id": "19463160#8",
    		"to_edge_id": "n/a",
    		"via_edge_id": "19463160#8",
    	    "flow_rate": "600",
    		"latitude": "36.137234",
    		"longitude": "-86.800842",
    		"removable": "1"}
        ],
        "west_lane_out":"19456179#0",
	    "west_lane_out_values":["19456179#0_0","19456179#0_1"],
	    "west_lane_in":"-19456179#0",
	    "west_lane_in_values":["-19456179#0_1", "-19456179#0_0"],
	    # left, straight, right
	    "west_lane_in_adjascent":["-19463160#7", "-19479801#4", "19463160#8"],

	    "east_lane_in":"19479801#4",
	    "east_lane_in_values":["19479801#4_0","19479801#4_1"],
	    "east_lane_in_adjascent":["19463160#8", "19456179#0", "-19463160#7"],
	    "east_lane_out":"-19479801#4",
	    "east_lane_out_values":["-19479801#4_1", "-19479801#4_0"],

	    "north_lane_in":"19463160#7",
	    "north_lane_in_values":["19463160#7_0","19463160#7_1"],
	    "north_lane_in_adjascent":["-19479801#4", "19463160#8", "19456179#0"],
	    "north_lane_out":"-19463160#7",
	    "north_lane_out_values":["-19463160#7_1","-19463160#7_0"],

	    "south_lane_out":"19463160#8",
	    "south_lane_out_values":["19463160#8_0","19463160#8_1"],
	    "south_lane_in":"-19463160#8",
	    "south_lane_in_values":["-19463160#8_1", "-19463160#8_0"],
	    "south_lane_in_adjascent":["19456179#0", "-19463160#7", "-19479801#4"],
        "induction_loop": {
            "19456179#0_0_5": {
                "location": "west_lane_out",
        	    "pos": 5
            },
            "19456179#0_1_5": {
                "location": "west_lane_out",
        	    "pos": 5
            },
            "-19456179#0_0_-5": {
                "location": "west_lane_in",
        	    "pos": -5
            },
            "-19456179#0_1_-5": {
                "location": "west_lane_in",
        	    "pos": -5
            },
            "-19479801#4_0_5": {
                "location": "east_lane_out",
        	    "pos": 5
            },
            "-19479801#4_1_5": {
                "location": "east_lane_out",
        	    "pos": 5
            },
            "19479801#4_0_-5": {
                "location": "east_lane_in",
        	    "pos": -5
            },
            "19479801#4_1_-5": {
                "location": "east_lane_in",
        	    "pos": -5
            },
            "-19463160#7_0_5": {
                "location": "north_lane_out",
        	    "pos": 5
            },
            "-19463160#7_1_5": {
                "location": "north_lane_out",
        	    "pos": 5
            },
            "19463160#7_0_-5": {
                "location": "north_lane_in",
        	    "pos": -5
            },
            "19463160#7_1_-5": {
                "location": "north_lane_in",
        	    "pos": -5
            },
            "19463160#8_0_5": {
                "location": "south_lane_out",
        	    "pos": 5
            },
            "19463160#8_1_5": {
                "location": "south_lane_out",
        	    "pos": 5
            },
            "-19463160#8_0_-5": {
                "location": "south_lane_in",
        	    "pos": -5
            },
            "-19463160#8_1_-5": {
                "location": "south_lane_in",
        	    "pos": -5
            }
        }
    }

    vehicleData = {
        "Car": {
            "name": "Car",
            "accel": "20",
    		"decel": "30",
    		"sigma": "1",
    		"max_speed": "100",
    		"length": "10",
    		"probability": "0.5"
        },
        "Bus": {
            "name": "Bus",
            "accel": "15",
    		"decel": "25",
    		"sigma": "1",
    		"max_speed": "70",
    		"length": "15",
    		"probability": "0.3"
        },
        "Truck": {
            "name": "Truck",
            "accel": "10",
    		"decel": "15",
    		"sigma": "1",
    		"max_speed": "50",
    		"length": "20",
    		"probability": "0.2"
        }
    }

    db.problem.insert_one({
        "problem_number": "3",
        "title": "Analyze the effects of vehicle parameters for a 4-way stop sign:",
        "description":"How do vehicle acceleration, deceleration, max speed, and length affect the average waiting time and average speed of the vehicles?  How are vehicle throughput (flow rate), queue length and queue duration at the assigned intersection affected? Report the impact of vehicle parameters.",
        "problem_area_id": problemArea,
        "default_config": {
            "map_loc_prefix": mapLocation + "westend_all_way",
            "type": "STOP_SIGN",
            "junctions": { junction1["_id"]: junction1, junction2["_id"]: junction2 },
            "vehicle_data": vehicleData
        }
    })

    db.problem.insert_one({
        "problem_number": "6a",
        "title": "Analyze the effects of traffic flows, vehicle types, turning probabilities for unprotected left turns:",
        "description":"Compare the three mechanisms based on the average waiting time, average speed, vehicle throughput (flow rate), and queue length and queue duration at the intersection. Based on these, can you suggest in what scenarios you prefer one over the other? Some mechanisms provide better performance (in terms of waiting time etc.) however, what could be drawbacks of those mechanisms? Change the vehicle flow rate and make vehicle type homogeneous by making other vehicle probability as zero. How does this impact the results?",
        "problem_area_id": problemArea,
        "default_config": {
            "map_loc_prefix": mapLocation + "westend_priority",
            "type": "UNPROTECTED",
            "junctions": { junction1["_id"]: junction1, junction2["_id"]: junction2 },
            "vehicle_data": vehicleData
        }
    })

    db.problem.insert_one({
        "problem_number": "6b",
        "title": "Analyze the effects of traffic flows, vehicle types, turning probabilities for left turns with stop sign:",
        "description":"Compare the three mechanisms based on the average waiting time, average speed, vehicle throughput (flow rate), and queue length and queue duration at the intersection. Based on these, can you suggest in what scenarios you prefer one over the other? Some mechanisms provide better performance (in terms of waiting time etc.) however, what could be drawbacks of those mechanisms? Change the vehicle flow rate and make vehicle type homogeneous by making other vehicle probability as zero. How does this impact the results?",
        "problem_area_id": problemArea,
        "default_config": {
            "map_loc_prefix": mapLocation + "westend_all_way",
            "type": "STOP_SIGN",
            "junctions": { junction1["_id"]: junction1, junction2["_id"]: junction2 },
            "vehicle_data": vehicleData
        }
    })

    junction1_6c = junction1.copy()
    junction1_6c["traffic_data"] = createTrafficData(True)
    junction2_6c = junction2.copy()
    junction2_6c["traffic_data"] = createTrafficData(True)

    db.problem.insert_one({
        "problem_number": "6c",
        "title": "Analyze the effects of traffic flows, vehicle types, turning probabilities for left turns with traffic lights:",
        "description":"Compare the three mechanisms based on the average waiting time, average speed, vehicle throughput (flow rate), and queue length and queue duration at the intersection. Based on these, can you suggest in what scenarios you prefer one over the other? Some mechanisms provide better performance (in terms of waiting time etc.) however, what could be drawbacks of those mechanisms? Change the vehicle flow rate and make vehicle type homogeneous by making other vehicle probability as zero. How does this impact the results?",
        "problem_area_id": problemArea,
        "default_config": {
            "map_loc_prefix": mapLocation + "westend_traffic",
            "type": "TRAFFIC_SIGNAL",
            "junctions": { junction1_6c["_id"]: junction1_6c, junction2_6c["_id"]: junction2_6c },
            "vehicle_data": vehicleData
        }
    })

    db.problem.insert_one({
        "problem_number": "8",
        "title": "Model the traffic lights at a single intersection that you have been put in charge of",
        "description":"Try out values for your traffic light timing sequences, with the goal of finding the right timing sequence that maximizes the flow of traffic through your intersection. Remember the flow is measured by the throughput parameter that was discussed in the last unit.",
        "problem_area_id": problemArea,
        "default_config": {
            "map_loc_prefix": mapLocation + "westend_traffic",
            "type": "TRAFFIC_SIGNAL",
            "junctions": { junction1["_id"]: junction1, junction2["_id"]: junction2 },
            "vehicle_data": vehicleData
        }
    })

    db.problem.insert_one({
        "problem_number": "10a",
        "title": "Optimize traffic light phases to improve traffic through your intersection:",
        "description":"By experimenting with the timing of the traffic light phases, try to produce the minimum average wait time at both intersections (with the default vehicle parameters, turning probabilities, and traffic input flow rates)? Based on these results, how would you describe a general approach that traffic engineers could follow for programming traffic lights?",
        "problem_area_id": problemArea,
        "default_config": {
            "map_loc_prefix": mapLocation + "westend_traffic",
            "type": "TRAFFIC_SIGNAL",
            "junctions": { junction1["_id"]: junction1, junction2["_id"]: junction2 },
            "vehicle_data": vehicleData
        }
    })

    db.problem.insert_one({
        "problem_number": "10b",
        "title": "Analyze the effects of driver behavior:",
        "description":"A basic model of driver behavior in traffic simulations uses a parameter called driver imperfection, which describes the extent to which drivers allow their speed to fluctuate instead of maintaining a constant speed. These fluctuations affect the vehicles behind a driver, which have to react to the driver's changing speed. By experimenting with different values for the driver imperfection parameter in this simulation, describe and generate plots of how this aspect of driver behavior impacts the average wait time.",
        "problem_area_id": problemArea,
        "default_config": {
            "map_loc_prefix": mapLocation + "westend_traffic",
            "type": "TRAFFIC_SIGNAL",
            "junctions": { junction1["_id"]: junction1, junction2["_id"]: junction2 },
            "vehicle_data": vehicleData
        }
    })

    db.problem.insert_one({
        "problem_number": "10c",
        "title": "Analyze the effects of lane closures:",
        "description":"How does closing one lane (which will reroute vehicles to other lanes) affect the average wait time? You can simulate a lane closure by adjusting the turning probabilities at an intersection so the vehicles will never enter the lane. Experiment to identify changes that can decrease the average wait time with the lane closure.",
        "problem_area_id": problemArea,
        "default_config": {
            "map_loc_prefix": mapLocation + "westend_traffic",
            "type": "TRAFFIC_SIGNAL",
            "junctions": { junction1["_id"]: junction1, junction2["_id"]: junction2 },
            "vehicle_data": vehicleData
        }
    })
