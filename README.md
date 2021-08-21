# Twitter Progress Bar

Twitter progress bar on profile image based on followers count

基于关注者数量的头像进度条

<a href="https://twitter.com/KumaTea0/photo" target="_blank">
  <img src="https://s.kmtea.eu/prog/avatar.png" alt="avatar" style="border-radius: 50%" width="200" height="200">
</a>

## Process

1. Get the followers count, pick the last two digits
2. Calculate [the angle of the sector](coord.py#L7) based on the percentage
3. We want it starts from the y-axis. Compute [the tangent](coord.py#L11)
4. Since we get the tangent, we can [get the shape of the polygon by its coordinates](coord.py#L27)
5. [Crop the progress bar](image.py#L16)<br>(NumPy helps a lot: it generates the cropped image in the original size, so we no longer need to calculate the merging anchor of a fragmented image)
6. [Merge](image.py#L50) the progress bar into the profile image

### Note

You will need [Twitter API Access](https://developer.twitter.com/) for this project.
If not, you may also seek a trusted friend and ask for an auth.
