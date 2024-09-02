import bpy


ratio = 0.5


total_polygons_before = 0
total_polygons_after = 0


selected_objects = bpy.context.selected_objects


print(f"Number of selected objects: {len(selected_objects)}")


objects_to_process = []


for obj in selected_objects:
    if obj.type == 'MESH':
        poly_count = len(obj.data.polygons)
        total_polygons_before += poly_count
        if not obj.data.shape_keys:
            objects_to_process.append(obj)
        else:
            print(f"Skipping object '{obj.name}' because it has shape keys.")
        print(f"Object: {obj.name}, Polygons before decimation: {poly_count}")


print(f"Number of objects to process: {len(objects_to_process)}")


for index, obj in enumerate(objects_to_process):
    print(f"Processing object {index + 1}/{len(objects_to_process)}: {obj.name}")
    
  
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj
    

    decimate = obj.modifiers.new(name="DecimateMod", type='DECIMATE')
    decimate.ratio = ratio
    bpy.ops.object.modifier_apply(modifier="DecimateMod")
    
 
    poly_count_after = len(obj.data.polygons)
    total_polygons_after += poly_count_after
    
    print(f"'Decimate' modifier applied to object: {obj.name}")
    print(f"Polygons after decimation: {poly_count_after}")
    

    obj.select_set(False)


print(f"Total number of polygons before decimation: {total_polygons_before}")
print(f"Total number of polygons after decimation: {total_polygons_after}")
print("Processing completed.")
