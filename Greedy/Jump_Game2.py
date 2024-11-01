def jump_game_two(nums):
  farthest_jump = 0
  current_jump = 0
  jumps = 0

  for i in range(len(nums) - 1):
    farthest_jump = max(farthest_jump, i + nums[i])

    if i == current_jump:
      jumps += 1
      current_jump = farthest_jump

      if current_jump >= len(nums) - 1:
        break

  return jumps

print(jump_game_two([2, 1, 1, 1, 4]))
