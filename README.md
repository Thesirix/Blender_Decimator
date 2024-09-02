# Decimation Script for Blender

This script is designed to simplify the process of decimating 3D models in Blender by reducing the polygon count of selected objects. It is especially useful for optimizing models by reducing their polygon count, which can improve performance in various applications such as gaming, animation, and real-time rendering.

## Features

- **Automatic Decimation**: The script automatically applies a decimation modifier to selected mesh objects, reducing their polygon count.
- **Exclusion of Objects with Shape Keys**: Objects that have shape keys are automatically skipped, ensuring that their deformations and animations are preserved.
- **Customizable Decimation Ratio**: The decimation level can be easily adjusted by changing the `ratio` variable. By default, it is set to `0.5`, meaning the polygon count will be reduced by half.

## Usage Instructions

1. **Select Objects**: To decimate objects in your scene, you must first select them. If you want to decimate all objects in your scene, press the `A` key to select everything.

2. **Run the Script**: Once your objects are selected, run the script in Blender's scripting editor. The script will automatically apply the decimation modifier to all selected mesh objects that do not have shape keys.

3. **Adjust Decimation Ratio**: If you need to change the decimation level, modify the `ratio` variable in the script. For example, setting `ratio = 0.5` will reduce the polygon count by half.

## Example

Here’s how the `ratio` variable works:
- `ratio = 0.5` (default): Reduces the polygon count by 50% (half the original).
- `ratio = 0.25`: Reduces the polygon count to 25% of the original (one-fourth).
- `ratio = 0.75`: Reduces the polygon count to 75% of the original.

By adjusting this ratio, you can control the level of detail retained in your models.

## Notes

- **Shape Keys**: Objects with shape keys are skipped to avoid losing shape key data, which is critical for certain animations and deformations.
- **Batch Processing**: The script processes all selected mesh objects in one go, making it easy to optimize large scenes with many objects.

## Conclusion

This script provides a quick and efficient way to decimate multiple objects in Blender while preserving important animation data. By adjusting the decimation ratio, you can easily balance between model detail and performance.

Happy modeling!
# Blender_Decimator
