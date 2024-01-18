class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: -x[1])
        total_units = 0
        boxes_added = 0
        
        for boxes, units_per_box in boxTypes:

            # Check if adding all remaining boxes fits in the truck
            if boxes_added + boxes <= truckSize:
                total_units += (boxes * units_per_box)
                boxes_added += boxes
            else:
                # If adding all remaining boxes exceeds truckSize, add as many as possible
                remaining_boxes = truckSize - boxes_added
                total_units += (remaining_boxes * units_per_box)
                break  # Stop adding boxes since the truck is full
                
        return total_units
        
