/// <reference path="../pb_data/types.d.ts" />
migrate((app) => {
  const collection = app.findCollectionByNameOrId("pbc_2722998921")

  // remove field
  collection.fields.removeById("geoPoint1587448267")

  return app.save(collection)
}, (app) => {
  const collection = app.findCollectionByNameOrId("pbc_2722998921")

  // add field
  collection.fields.addAt(3, new Field({
    "hidden": false,
    "id": "geoPoint1587448267",
    "name": "location",
    "presentable": false,
    "required": false,
    "system": false,
    "type": "geoPoint"
  }))

  return app.save(collection)
})
