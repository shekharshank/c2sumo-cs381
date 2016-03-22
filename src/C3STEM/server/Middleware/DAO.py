from bson.objectid import ObjectId
from datetime import datetime
from DBUtil import *
from default_problem_data import setSimulationToDefault
from SimulationBackupInterface import *
import logging
from UserDataDAO import getGroupTypeDB

class SimulationDAO(object):

	def getIntersectionIDs(self, simulation_id):
		""" Get intersection IDs associated
		with simulation id
		"""
		db = DBUtil().getDatabase()
		simulation = db.simulation.find_one({"_id": ObjectId(simulation_id)})
		problem = db.problem.find_one({"_id": simulation["problem_id"]})
		return problem["default_config"]["junctions"]

	def getRestOfIntersectionIDs(self, simulation_id):
		""" Get rest of the intersection IDs
		in the simulation id
		"""
		junctions = getIntersectionIDs(simulation_id)
		assoc_junctions = []
		for junction_id in junctions:
			if junction_id['_id'] != actual_junction[0]:
				assoc_junctions.append(junction_id['_id'])
		return assoc_junctions

class VehiclesDAO(object):
	def readAllVehicles(self, simulation_id):
		""" Reads vehicles from vehicles table
			gets simulation id
		"""
		db = DBUtil().getDatabase()
		cursor = db.simulation_instance.find({})
		vehicles = []
		for record in cursor:
			vehicles.extend(readVehicles(record["_id"]))
		return vehicles

	def readVehicles(self, simulation_id):
		""" Reads vehicles from vehicles table
			gets simulation id
		"""
		db = DBUtil().getDatabase()
		simulation = db.simulation_instance.find_one({"_id": simulation_id})
		vehicles = []
		# convert dictionary to list
		for _id, data in simulation["config"]["vehicle_data"]:
			vehicles.append(data)
		return vehicles

	def deleteVehicle(self, simulation_id, vehicle_id):
		""" Delete vehicles from vehicles table
			gets vehicle id
		"""
		db = DBUtil().getDatabase()
		simulation = db.simulation_instance.find_one({"_id": simulation_id})
		del simulation["config"]["vehicle_data"][vehicle_id]
		db.simulation_instance.save(simulation)

	def updateVehicle(self, vehicle_id, accel, decel, sigma, max_speed, length, probability):
		""" Update vehicle from vehicles table
			gets vehicle id and updated params
		"""
		db = DBUtil().getDatabase()
		simulation = db.simulation_instance.find_one({"_id": simulation_id})
		found = simulation["config"]["vehicle_data"][vehicle_id]
		found["_id"] = ObjectId(vehicle_id)
		#found["name"] = name
		found["accel"] = accel
		found["decel"] = decel
		found["sigma"] = sigma
		found["max_speed"] = max_speed
		found["length"] = length
		found["probability"] = probability
		db.simulation_instance.save(simulation)

	def createVehicle(self, simulation_id, name, accel, decel, sigma, max_speed, length, probability):
		""" Create vehicle into vehicles table
			gets params
		"""
		db = DBUtil().getDatabase()
		simulation = db.simulation_instance.find_one({"_id": simulation_id})
		# NOTE: this will silently update a vehicle's record if there is a name collision
		simulation["config"]["vehicle_data"][name] = {
			"name": name,
			"accel": accel,
			"decel": decel,
			"sigma": sigma,
			"max_speed": max_speed,
			"length": length,
			"probability": probability
		}
		db.simulation_instance.save(simulation)

class FlowsDAO(object):
	# TODO: update to new database model
	def readAllFlows(self, simulation_id):
		""" Reads all flows
			gets simulation id
		"""
		db = DBUtil().getDatabase()
		flowPoints = db.flows.find({"simulation_id": ObjectId(simulation_id)})
		return flowPoints

	def readFlow(self, simulation_id, point_name):
		""" Reads vehicles from vehicles table
			gets simulation id
		"""
		db = DBUtil().getDatabase()
		flow = db.flows.find_one({"simulation_id": ObjectId(simulation_id), "point_name": point_name})
		return flow

	def deleteFlow(self, simulation_id, point_name):
		""" Not implemented
			Yet
		"""
		db = DBUtil().getDatabase()

	def createFlow(self, simulation_id, point_name):
		""" Not implemented
			yet
		"""
		db = DBUtil().getDatabase()

	def updateFlow(self, simulation_id, point_name, flow_rate):
		""" Update Flow table
			based on the parameters being passed
		"""

		db = DBUtil().getDatabase()
		found = db.flows.find_one({"simulation_id": ObjectId(simulation_id), "point_name": point_name})
		found["flow_rate"] = flow_rate
		db.flows.save(found)

class TurnProbabilityDAO(object):

	def readAllTurnProbabilities(self, simulation_id, intersection_id):
		# pretty complicated to write with the new database structure
		""" Reads vehicles from vehicles table
			gets simulation id
		"""
		# db = DBUtil().getDatabase()
		# turn = db.turnprobability.find({"simulation_id": ObjectId(simulation_id), "intersection_id": intersection_id})
		return None

	def readTurnProbability(self, simulation_id, edge_id):
		""" Reads vehicles from vehicles table
			gets simulation id
		"""
		db = DBUtil().getDatabase()
		simulation = db.simulation_instance.find_one({"_id": simulation_id})
		for junction in simulation["config"]["junctions"]:
			if edge_id in junction["turn_probability"]:
				return junction["turn_probability"][edge_id]
		# could not find the proper edge_id
		return None

	def deleteTurnProbability(self, edge_id):
		""" Not implemented
			Yet
		"""
		db = DBUtil().getDatabase()

	def createTurnProbability(self, edge_id):
		""" Not implemented
			yet
		"""
		db = DBUtil().getDatabase()

	def updateTurnProbability(self, simulation_id, edge_id, left_turn, right_turn, go_straight):
		""" Update turn probability table
			based on the parameters being passed
		"""

		db = DBUtil().getDatabase()
		simulation = db.simulation_instance.find_one({"_id": simulation_id})
		for junction in simulation["config"]["junctions"]:
			if edge_id in junction["turn_probability"]:
				edge = junction["turn_probability"][edge_id]
				edge["left_turn"] = left_turn
				edge["right_turn"] = right_turn
				edge["go_straight"] = go_straight
		db.simulation_instance.save(simulation)

class TrafficLightDAO(object):

	def readAllTrafficLightLogic(self, simulation_id, intersection_id):
		# pretty complicated to write with the new database structure
		""" Reads traffic light logic from traffic light table
			gets traffic light id
		"""
		# db = DBUtil().getDatabase()
		# traffic_light_logic = db.trafficlightlogic.find({ "simulation_id": ObjectId(simulation_id), "intersection_id": intersection_id }).sort([("creation_time", 1)])
		# return traffic_light_logic
		return None

	def readTrafficLightLogic(self, simulation_id, intersection_id):
		""" Reads traffic light logic from traffic light table
			gets traffic light id
		"""
		db = DBUtil().getDatabase()
		traffic_light_logic = db.simulation_instance.find_one({"_id": simulation_id})["config"]["junctions"][intersection_id]["traffic_data"]
		return traffic_light_logic

	def deleteTrafficLightLogic(self, simulation_id, intersection_id, state):
		""" Delete traffic light logic from traffic light table
			 gets vehicle id
		"""
		db = DBUtil().getDatabase()
		simulation = db.simulation_instance.find_one({"_id": simulation_id})
		traffic_light_logic = simulation["config"]["junctions"][intersection_id]["traffic_data"]
		# NOTE: fails silently if the specific state is not found
		for instance in traffic_light_logic:
			if instance.state == state:
				traffic_light_logic.remove(instance)
				db.simulation_instance.save(simulation)
				return

	def createTrafficLightLogic(self, simulation_id, intersection_id, state, duration):
		""" Create vehicle into vehicles table
			gets params
			light_index = 0!1!2 is passed as this format
		"""
		db = DBUtil().getDatabase()
		simulation = db.simulation_instance.find_one({"_id": simulation_id})
		traffic_light_logic = simulation["config"]["junctions"][intersection_id]["traffic_data"]
		traffic_light_logic.append({ "state": state, "duration": duration })
		db.simulation_instance.save(simulation)

	def updateTrafficLightLogic(self, simulation_id, intersection_id, state, duration):
		""" Update traffic light logic table
			gets id and updated params
		"""
		db = DBUtil().getDatabase()
		simulation = db.simulation_instance.find_one({"_id": simulation_id})
		traffic_light_logic = simulation["config"]["junctions"][intersection_id]["traffic_data"]
		for instance in traffic_light_logic:
			if instance.state == state:
				instance.duration = duration
				db.simulation_instance.save(simulation)
				return

	'''
	def updateTrafficLightLogic(self, id, state, duration):
		""" Update traffic light logic table
			gets id and updated params
		"""
		db = DBUtil().getDatabase()
		found = db.trafficlightlogic.find_one({"_id": ObjectId(id)})
		found["state"] = state
		found["duration"] = duration
		db.trafficlightlogic.save(found)

		found_asso = db.trafficlightlogic.find({"associated_with_id": ObjectId(id)})
		for find in found_asso:
			find["state"] = state
			find["duration"] = duration
			db.trafficlightlogic.save(find)
	'''
class SimAssociationDAO(object):
	# NOTE: I don't think these methods are necessary anymore
	def readAssociatedSimIDs(self, simulation_id):
		""" Gets actual simulation id and
			finds all the associated simulation ids with it
		"""
		db = DBUtil().getDatabase()
		print simulation_id
		assoc_ids= db.simulation_association.find_one({ "sim_id": ObjectId(simulation_id)})
		vals = assoc_ids["sim_asso"]
		return vals

	def getOrigIdForAssociatedSimID(self, asso_id):
		db = DBUtil().getDatabase()
		asso_records = db.simulation_association.find({ "sim_asso": ObjectId(asso_id)} )
		sim_id = None
		for record in asso_records:
			sim_id = record['sim_id']
			if record.get('is_master') is not None and record.get('is_master'):
				return sim_id;
		return sim_id

class StudentGroupDAO(object):
	def readAllGroupNames(self):
		""" Get all the group names for the collaboration
		"""
		db = DBUtil().getDatabase()
		groups = db.group.find({"name": {"$in": ["1","2","3","4","5","6","7","8","9","10"]}}).sort([("name", 1)])
		return groups

	def readGroupNames(self, id):
		""" Get all the group names for the collaboration
		"""
		db = DBUtil().getDatabase()
		found = db.group.find_one({"_id": id})
		return found

	def updateCollaborationUrl(self, id, collaboration_url):
		""" Update url for the hangout
		"""
		db = DBUtil().getDatabase()
		found = db.group.find_one({"_id": id})
		found["collaboration_url"] = collaboration_url
		# found["last_update_time"] = str(datetime.now())
		db.studentgroup.save(found)

	def getCollaborationUrl(self, id):
		""" Get url for the hangout
		"""
		db = DBUtil().getDatabase()
		found = db.group.find_one({"_id": id})
		return found

class ProblemsDAO(object):
	def readAllProblems(self):
		""" Reads all problems
		"""
		db = DBUtil().getDatabase()
		problems = db.problem.find()
		return problems

	def readProblem(self, problem_id):
		""" Read problem from problems table
		"""
		db = DBUtil().getDatabase()
		problem = db.problem.find_one({"_id": problem_id})
		return problem

	def getProblemID(self, simulation_instance_id):
		""" Return the problem ID that student is
			working on
		"""
		db = DBUtil().getDatabase()
		found = db.simulation_instance.find_one({"_id": ObjectId(simulation_instance_id)})
		simulation = db.simulation.find_one({"_id": found["simulation_id"]})
		return simulation["problem_id"]

	def updateProblem(self, simulation_id, problem_id):
		# NOTE: I don't think this is necessary with the new database design
		""" Update the problem that student is
			working on
		"""
		return None
		# db = DBUtil().getDatabase()
		# found = db.simulation.find_one({"_id": ObjectId(simulation_id)})
		# found["problem_id"] = problem_id
		# db.simulation.save(found)
		#
		# db.problems.update({"problem_id" : problem_id}, {"$push" : {"history" : {"update_time": datetime.now(), "simulation_id" : simulation_id} } })
		#
		# asso_simids = SimAssociationDAO().readAssociatedSimIDs(simulation_id)
		# for sim_id in asso_simids:
		# 	logging.info('sim_id: ' + str(sim_id))
		# 	db.simulation.update ({"_id": sim_id}, {  '$set': { 'problem_id': problem_id}})
		# 	# FORGOT TO ADD THE LOGIC EARLIER, QUICKFIX FOR NOW
		# 	SimulationBackupInterface(simulation_id).backupSimulation("SYSTEM", "PROBLEM_UPDATED")
		# 	simdata = db.simulation.find_one({"_id": sim_id})
		# 	intersection_id = "202305472"
		# 	if (simdata is not None):
		# 		group_type = getGroupTypeDB(simdata['group_id'])
		# 		if (group_type is not None) and (group_type == 'B'):
		# 			intersection_id = "202305458"
		# 	setSimulationToDefault(sim_id, problem_id, intersection_id)



class ReasonDAO(object):
	def createReason(self, simulation_id, user_id, problem_id, desc):
		""" Create reason for changing parameters into reason_change table
		"""
		db = DBUtil().getDatabase()
		db.reason_change.insert({
			"simulation_id": simulation_id,
			"user_id": user_id,
			"problem_id": problem_id,
			"description": desc,
			"creation_time": str(datetime.now())
		})

class ColabLogDAO(object):
	def createLog(self, simulation_id, user_id, problem_id):
		""" Log collaboration history
		"""
		db = DBUtil().getDatabase()
		db.colab_log.insert({
			"simulation_id": simulation_id,
			"user_id": user_id,
			"problem_id": problem_id,
			"colab_time": str(datetime.now())
		})

	def readCollaboration(self, user_id):
		db = DBUtil().getDatabase()
		colabs = db.colab_log.find({"user_id": user_id}).sort([("colab_time", 1)])
		return colabs
