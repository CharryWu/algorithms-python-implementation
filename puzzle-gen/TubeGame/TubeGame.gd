extends Node2D

export (int) var container_top = 200
export (int) var container_left = 100
export (int) var num_rows = 4
export (int) var num_cols = 3
export (int) var tube_block_size = 225
export (int) var x_shape_occurrence_percentage = 100
export (bool) var debug = true

onready var TubeBlockI = preload("res://UI/TubeGame/TubeBlock/TubeBlockI.tscn")
onready var TubeBlockL = preload("res://UI/TubeGame/TubeBlock/TubeBlockL.tscn")
onready var TubeBlockT = preload("res://UI/TubeGame/TubeBlock/TubeBlockT.tscn")
onready var TubeBlockX = preload("res://UI/TubeGame/TubeBlock/TubeBlockX.tscn")
onready var TubeBlockEnter = preload("res://UI/TubeGame/TubeBlock/TubeBlockEnter.tscn")
onready var TubeBlockExit = preload("res://UI/TubeGame/TubeBlock/TubeBlockExit.tscn")
onready var container = $TubeBlocks

const UP = [-1, 0]
const RIGHT = [0, 1]
const DOWN = [1, 0]
const LEFT = [0, -1]
const DIR = [UP, RIGHT, DOWN, LEFT] # UP, RIGHT, DOWN, LEFT
const TUBEDIR_MAX = 4

var enter_col
var exit_col
var enterTubeBlock
var exitTubeBlock
var _tubeDirs = [] # bit representation of tubedirs
var tubes = [] # generated data for every tube
var tubeBlocks = [] # ref to all tubeblocks

# Called when the node enters the scene tree for the first time.
func _ready():
	container.translate(Vector2(container_left, container_top))
	_initArrays()
	randomize()

	var verified = false
	while not verified:
		tubes = generateTubes()
		var attempts = [] # [enter_col, exit_col] tuples
		enter_col = randi() % num_cols
		exit_col = randi() % num_cols
		while not verified and attempts.size() < num_cols*num_cols:
			# try all (entry,exit) combinations, if not work, add to attemps array
			while attempts.has([enter_col, exit_col]): # skip tried (and failed) (entry,exit)
				enter_col = randi() % num_cols
				exit_col = randi() % num_cols
			if debug: printBlocks(tubes, enter_col, exit_col)
			verified = verifySolution(tubes, enter_col, exit_col)
			attempts.append([enter_col, exit_col])
		# if all pairs of (enter_col, exit_col) doesn't work for given tubes, regenerate tubes

	# POSTCOND: succesfully verify solution for generated (tubes, enter_col, exit_col)
	layoutTubes(container, tubes, enter_col, exit_col)

func printBlocks(tubes, enter_col, exit_col):
	"""
	Helper function to print out the generated blocks types and entry/exit point
	Used for debugging
	"""
	var firstRow = ""
	for i in range(num_cols):
		if i == enter_col:
			firstRow += '↓'
		else:
			firstRow += ' '
	print(firstRow)
	for row in tubes:
		var rowstr = ""
		for item in row:
			if item[0] == TubeBlockType.I:
				rowstr += 'I'
			elif item[0] == TubeBlockType.L:
				rowstr += 'L'
			elif item[0] == TubeBlockType.T:
				rowstr += 'T'
			elif item[0] == TubeBlockType.X:
				rowstr += 'X'
		print(rowstr)
	var lastRow = ""
	for i in range(num_cols):
		if i == exit_col:
			lastRow += '↓'
		else:
			lastRow += ' '
	print(lastRow)

func _initArrays():
	for i in range(num_rows):
		_tubeDirs.append([])
		tubes.append([])
		tubeBlocks.append([])
		for j in range(num_cols):
			_tubeDirs[i].append([])
			tubes[i].append([null, null])
			tubeBlocks[i].append(null)

func isInbound(row, col):
	return 0 <= row and row < num_rows and 0 <= col and col < num_cols

func genDirs():
	"""
	Pre-generate the directions at all blocks that connects (start, end) point
	The _tubeDirs info can be later used to generate the tube block type
	Uses Prim's MST algorithm
	"""
	var start_point = [randi()%num_rows, randi()%num_cols] # random start point
	var queue = [start_point] # array of 2D coordinates
	
	while not queue.empty():
		var cur_idx = randi() % queue.size()
		var cur = queue[cur_idx]
		var cur_row = cur[0]
		var cur_col = cur[1]
		var dir = DIR[randi() % DIR.size()] # select random direction for next node

		# check if current node directions are fully generated
		if _tubeDirs[cur_row][cur_col].size() == TUBEDIR_MAX:
			if debug: print("Generated X Shape Block @ (", cur_row, ",", cur_col, ")")
			queue.remove(cur_idx)
			continue
		elif _tubeDirs[cur_row][cur_col].size() == TUBEDIR_MAX-1:
			if randi() % 100 >= x_shape_occurrence_percentage:
				continue

		var generate_completed: bool = true
		for D in DIR: # check neighbors before proceeding with next node
			var nrow = cur_row + D[0]
			var ncol = cur_col + D[1]
			if isInbound(nrow, ncol) and _tubeDirs[nrow][ncol].empty():
				generate_completed = false # continue if any neighbor is not generated
		if generate_completed: # skip if all neighbors have been fully generated
			queue.remove(cur_idx)
			continue

		var next_row = cur_row + dir[0]
		var next_col = cur_col + dir[1]
		if not isInbound(next_row, next_col) or _tubeDirs[next_row][next_col].size() > 0:
			continue # skip if next node out of bound or direction already generated
		_tubeDirs[cur_row][cur_col].append(dir)
		_tubeDirs[next_row][next_col].append([-dir[0], -dir[1]])
		queue.append([next_row, next_col])

func _isBlockI(dir1, dir2):
	return dir1[0] == -dir2[0] and dir1[1] == -dir1[1]
#[
#	[
#		[TubeBlockType.I, Orientation.UP],
#		[TubeBlockType.T, Orientation.LEFT],
#		[TubeBlockType.I, Orientation.LEFT],
#	], [
#		[TubeBlockType.I, Orientation.UP],
#		[TubeBlockType.L, Orientation.LEFT],
#		[TubeBlockType.L, Orientation.LEFT],
#	], [
#		[TubeBlockType.I, Orientation.UP],
#		[TubeBlockType.X, Orientation.LEFT],
#		[TubeBlockType.I, Orientation.LEFT],
#	], [
#		[TubeBlockType.T, Orientation.LEFT],
#		[TubeBlockType.I, Orientation.LEFT],
#		[TubeBlockType.L, Orientation.LEFT],
#	]
#]
func generateTubes():
	genDirs()
	for row in _tubeDirs.size():
		for col in _tubeDirs[row].size():
			var dir = _tubeDirs[row][col]
			var type = TubeBlockType.I # default use block I
			var orientation = Orientation.UP # default orientation up
			if dir.size() == 4:
				type = TubeBlockType.X
			elif dir.size() == 3:
				type = TubeBlockType.T
			elif dir.size() == 2:
				type = TubeBlockType.I if _isBlockI(dir[0], dir[1]) else TubeBlockType.L
			else:
				type = TubeBlockType.I
			var ori_rand = randi() % 4
			if ori_rand == 1:
				orientation = Orientation.RIGHT
			if ori_rand == 2:
				orientation = Orientation.DOWN
			if ori_rand == 3:
				orientation = Orientation.LEFT
			tubes[row][col] = [type, orientation]
	return tubes

func getNeighbors(row, col, type, enter_dir):
	"""
	Get the block position of reachable neighbors
	and entry direction based on cur block type
	"""
	var neighbors = []
	var enter_dx = enter_dir[1]
	var enter_dy = enter_dir[0]

	if type == TubeBlockType.I:
		if enter_dx == 0: # vertical
			neighbors.append([row-enter_dy, col, enter_dir])
		elif enter_dy == 0: # horizontal
			neighbors.append([row, col-enter_dx, enter_dir])
	# both L shape and T shape can exit at orthogonal direction
	elif type == TubeBlockType.L or type == TubeBlockType.T:
		if enter_dx == 0: # vertical
			neighbors.append([row, col+1, LEFT]) # exit to RIGHT
			neighbors.append([row, col-1, RIGHT]) # exit to LEFT
		elif enter_dy == 0: # horizontal
			neighbors.append([row+1, col, UP]) # exit to DOWN
			neighbors.append([row-1, col, DOWN]) # exit to UP
	elif type == TubeBlockType.X:
		var _DIR = DIR.duplicate()
		_DIR.erase(enter_dir)
		for d in _DIR:
			neighbors.append([row+d[0], col+d[1], [-d[0], -d[1]]])
	
	# remove out-of-bound neighbors
	for neighbor in neighbors:
		if not isInbound(neighbor[0], neighbor[1]):
			neighbors.erase(neighbor)
	return neighbors

func encode(row, col, dir):
	"""
	Encode block position and direction into string
	Used for the key of memoization - visited
	"""
	return str(row)+','+str(col)+','+str(dir)

func onPath(path, row, col):
	for p in path:
		if p[0] == row and p[1] == col:
			return true
	return false


func backtrack(row, col, dir, exit_row, exit_col, path, tubes, visited):
	"""
	DFS backtracking to verify if can reach (exit_row, exit_col) can be reached
	from (row, col) with the given solution - tubes
	"""
	if not isInbound(row, col):
		return false
	var enc = encode(row, col, dir)
	if enc in visited:
		return visited[enc]

	var type = tubes[row][col][0]
	if row == exit_row and col == exit_col:
		# check if can exit to bottom
		if type == TubeBlockType.L and dir == UP:
			visited[enc] = false
			return false # L shape can't exit bottom if entered from above
		if type == TubeBlockType.I and (dir == LEFT or dir == RIGHT):
			visited[enc] = false
			return false # I shape can't exit bottom if entered from left/right
		visited[enc] = true
		return true # T and X shape can bottom exit from any entry direction
	
	# mark visited
	path.append([row, col, dir])
	for neighbor in getNeighbors(row, col, type, dir):
		if not onPath(path, neighbor[0], neighbor[1]):
			if backtrack(neighbor[0], neighbor[1], neighbor[2], exit_row, exit_col, path, tubes, visited):
				visited[enc] = true
				return true
	path.pop_back()
	visited[enc] = false
	return false


func verifySolution(tubes, enter_col, exit_col):
	"""
	Set up solver and verify 
	"""
	var exit_row = num_rows-1
	var path = []
	var visited = {}
	# var start = [0, enter_col, [0, -1]]
	return backtrack(0, enter_col, UP, exit_row, exit_col, path, tubes, visited)

func layoutTubes(container, tubes, enter_col, exit_col):
	"""
	Move all blocks to correct position on screen
	"""
	var offsetX = tube_block_size / 2
	var offsetY = tube_block_size / 2

	enterTubeBlock = TubeBlockEnter.instance()
	enterTubeBlock.position.x = offsetX + enter_col * tube_block_size
	enterTubeBlock.position.y = -offsetY
	container.add_child(enterTubeBlock)

	for row in range(num_rows):
		for col in range(num_cols):
			var tube = tubes[row][col]
			var tubeType = tube[0]
			var tubeOrientation = tube[1]
			var tubeInstance
			# set tube type
			if tubeType == TubeBlockType.I:
				tubeInstance = TubeBlockI.instance()
			elif tubeType == TubeBlockType.L:
				tubeInstance = TubeBlockL.instance()
			elif tubeType == TubeBlockType.T:
				tubeInstance = TubeBlockT.instance()
			elif tubeType == TubeBlockType.X:
				tubeInstance = TubeBlockX.instance()
			# set orientation
			if tubeOrientation == Orientation.UP:
				pass
			elif tubeOrientation == Orientation.RIGHT:
				tubeInstance.rotation_degrees = 90
			elif tubeOrientation == Orientation.DOWN:
				tubeInstance.rotation_degrees = 180
			elif tubeOrientation == Orientation.LEFT:
				tubeInstance.rotation_degrees = -90
			tubeInstance.position.x = col * tube_block_size + offsetX
			tubeInstance.position.y = row * tube_block_size + offsetY
			tubeBlocks[row][col] = tubeInstance
			tubeInstance.get_node("TouchArea2D").connect("input_event",self,"_on_tube_block_input_event")
			container.add_child(tubeInstance)

	exitTubeBlock = TubeBlockExit.instance()
	exitTubeBlock.position.x = offsetX + exit_col * tube_block_size
	exitTubeBlock.position.y = offsetY + num_rows * tube_block_size
	container.add_child(exitTubeBlock)


func _on_tube_block_input_event( viewport, event, shape_idx ):
	"""
	Add custom events when a block is pressed
	"""
	if Input.is_action_just_released("click"):
		# TODO: check if there's a viable path from start to end
		pass
