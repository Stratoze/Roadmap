# AI projects

Project-based (learner, 2026-11-11). Rule: **a library tool is earned
only after building the small version yourself.** Data loading, windows
and drawing are not the skill, so those libraries are allowed from the
start; the math, the learning and the physics are written by hand first.
Python on the laptop. Code goes in the learner's own repo; a short note
and the "done when" evidence go on the `Result:` line.

Each milestone: SEARCH (keywords for YouTube or Google), Build, Done when.
Its ready mentor prompt: `bash Prompts/give.sh A1.1` (and so on).
Haiku gives the SEARCH line and the prompt, logs what is pasted, and
ticks when the learner reports the "done when" evidence.

## A1 Digit recognizer from scratch (Python; numpy earned at A1.1)

- [ ] **A1.1 Matrices.** SEARCH: 3Blue1Brown Essence of Linear Algebra,
  chapters 1-4. Build: matrix times vector and matrix times matrix in
  plain Python lists. Done when: your function matches numpy's `@` on a
  random 3x4 times 4x2. Earns: numpy.
  Result:
- [ ] **A1.2 One neuron learns.** SEARCH: 3Blue1Brown neural networks
  chapter 2, gradient descent. Build: fit y = 2x + 1 from noisy points
  with one weight and one bias, your own derivative. Done when: loss
  goes down every few steps, w is about 2 and b about 1.
  Result:
- [ ] **A1.3 Backpropagation.** SEARCH: 3Blue1Brown backpropagation
  (chapters 3-4); Karpathy "micrograd" video. Build: a 2-layer network
  solving XOR, gradients by hand. Done when: 4 of 4 XOR cases right, and
  your gradients match a numerical gradient check.
  Result:
- [ ] **A1.4 MNIST.** SEARCH: MNIST neural network from scratch numpy.
  Build: train your A1.3 network on MNIST (any loader allowed). Done
  when: at least 90% test accuracy, and you show the 10 worst mistakes
  and say why they are hard.
  Result:
- [ ] **A1.5 Earn PyTorch.** SEARCH: PyTorch MNIST tutorial. Build: the
  same network in PyTorch. Done when: similar accuracy, and you can say
  which line replaced which part of your own code. Earns: PyTorch.
  Result:

## Next projects (milestones keyed by Opus when A1 is near done)

- **A2 2D racing game.** pygame for window and drawing only; car
  physics (kinematic bicycle model, the same math as arm kinematics),
  collision and ray sensors by hand. Done when you can drive a lap with a
  timer.
- **A3 RL drives the car.** Q-learning from scratch on a grid world, then
  on the car with your ray sensors; then policy gradient with your A1
  network. Earns: Gymnasium and Stable-Baselines3 (PPO).
- **A4 Imitation learning.** Record your own driving, train your network
  to copy it (behavior cloning), compare with RL. This is what the
  SO-101 arm does with LeRobot (ACT): the bridge to the arm.
- **A5 Convolution from scratch.** A small CNN for digits by hand, then
  in PyTorch: the start of vision for the arm.
