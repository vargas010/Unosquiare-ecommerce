/// <reference path="../pb_data/types.d.ts" />
migrate((app) => {
  const collection = app.findCollectionByNameOrId("pbc_514518509")

  // remove field
  collection.fields.removeById("relation2220669758")

  return app.save(collection)
}, (app) => {
  const collection = app.findCollectionByNameOrId("pbc_514518509")

  // add field
  collection.fields.addAt(2, new Field({
    "cascadeDelete": false,
    "collectionId": "pbc_3705076665",
    "hidden": false,
    "id": "relation2220669758",
    "maxSelect": 1,
    "minSelect": 0,
    "name": "end_date",
    "presentable": false,
    "required": false,
    "system": false,
    "type": "relation"
  }))

  return app.save(collection)
})
