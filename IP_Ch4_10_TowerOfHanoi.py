# ================================================================================= Book Explanation
# Move a tower of height-1 to an intermediate pole, using the final pole.
# Move the remaining disk to the final pole.
# Move the tower of height-1 from the intermediate pole to the final pole using the original pole.
# if you were going to explicitly keep track of the disks, you would probably use three Stack objects,
#     one for each pole. The answer is that Python provides the stacks that we need implicitly through the call stack
# =================================================================================== My Solution
# Implementing the moveTower was simple enough from the outline
#     But I had no idea what to do for moveDisk
#     From the hint about the python call stack I knew it needed to be there, but I didn't know what it would do
#     As a placeholder I made it print, and thar worked perfectly
# ===================================================================================== differences
# The simplicity of the solution makes this pretty easy to code
#     Even though I did get thrown a bit by moveDisk()
# Without the hint to use the python call stack I definitely would've made explicit stacks for each pole
#     And also probably some sort of disk class

def moveTower(height, startPole, intermediatePole, endPole):
    if height>1:
        moveTower(height-1, startPole, endPole, intermediatePole)
    if height>0:
        moveDisk(startPole, endPole)
    if height>1:
        moveTower(height-1, intermediatePole, startPole, endPole)

def moveDisk(fromPole, toPole):
    print('movedisk FROM: %s TO: %s' % (fromPole, toPole))

moveTower(5, '0', '1', '2')