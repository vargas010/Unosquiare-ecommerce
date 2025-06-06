/// <reference path="../pb_data/types.d.ts" />
migrate((app) => {
  const collection = app.findCollectionByNameOrId("pbc_514518509")

  // add field
  collection.fields.addAt(4, new Field({
    "hidden": false,
    "id": "bool1397647488",
    "name": "work",
    "presentable": false,
    "required": false,
    "system": false,
    "type": "bool"
  }))

  return app.save(collection)
}, (app) => {
  const collection = app.findCollectionByNameOrId("pbc_514518509")

  // remove field
  collection.fields.removeById("bool1397647488")

  return app.save(collection)
})
