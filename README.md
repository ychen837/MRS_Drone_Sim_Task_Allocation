# MRS_Drone_Sim_Task_Allocation

test_task_alloc_offline.py: type 1 algorithm master node, assigns tasks before starting the simulation; to run this, first initialize uav by running task_posctl_test.
task_posctl_test.py: drone pose control node, accepts waypoint command from task allocation master, shuts down when master announce mission is completed

in work: type 2 algorithm, dynamically assign tasks when agents/drones are idling.
