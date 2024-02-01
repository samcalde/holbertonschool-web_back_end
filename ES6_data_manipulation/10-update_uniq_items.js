export default function updateUniqueItems(updateMap) {
  if (updateMap instanceof Map) {
    for (const dataMap of updateMap) {
      if (dataMap[1] === 1) {
        updateMap.set(dataMap[0], 100);
      }
    }
    return updateMap;
  }
  throw new Error('Cannot process');
}