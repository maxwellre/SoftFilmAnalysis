cmake_minimum_required(VERSION 3.16.3)

project(leapcmein VERSION "1.0.0" LANGUAGES C)

set(ULTRALEAP_PATH_ROOT "$ENV{ProgramFiles}/Ultraleap")

find_package(LeapSDK 4.1.0 PATHS "${CMAKE_CURRENT_LIST_DIR}/..")
	
add_library(
	ExampleConnection
	SHARED
	"libExampleConnection.c")

target_link_libraries(
	ExampleConnection
	PRIVATE
		LeapSDK::LeapC)

get_target_property(
	LEAPC_IMPORTED_CONFIG
	LeapSDK::LeapC
	IMPORTED_CONFIGURATIONS
)

get_target_property(
	LEAPC_SHARED_LIB_PATH
	LeapSDK::LeapC
	IMPORTED_LOCATION_${LEAPC_IMPORTED_CONFIG}
)

add_custom_command(
	TARGET
		ExampleConnection
	POST_BUILD
	COMMAND
		${CMAKE_COMMAND} -E copy
		${LEAPC_SHARED_LIB_PATH}
		$<TARGET_FILE_DIR:ExampleConnection>)

