# Twitter Progress Bar

Twitter progress bar on profile image based on followers count

基于关注着数量的头像进度条

## Process

1. Getting followers count, pick the last two digits
2. Calculate [the angle of the sector](coord.py#L7) based on the percentage
3. We want it starts from the y-axis. Compute [the tangent](coord.py#L11)
4. Since we get the tangent, we can [get the shape of the polygon by its coordinates](coord.py#L27)
5. [Crop the progress bar](image.py#L16)<br>(NumPy helped a lot: it generates the cropped image in the original size, so that we no longer need to calculate the merging anchor of a fragmented image)
6. [Merging](image.py#L50) the progress bar into the profile image
