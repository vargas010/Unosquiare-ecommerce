/// <reference path="../pb_data/types.d.ts" />
migrate((app) => {
  const collection = app.findCollectionByNameOrId("pbc_2376352475")

  // add field
  collection.fields.addAt(4, new Field({
    "cascadeDelete": false,
    "collectionId": "pbc_737954259",
    "hidden": false,
    "id": "relation1806832074",
    "maxSelect": 1,
    "minSelect": 0,
    "name": "Provider",
    "presentable": false,
    "required": false,
    "system": false,
    "type": "relation"
  }))

  return app.save(collection)
}, (app) => {
  const collection = app.findCollectionByNameOrId("pbc_2376352475")

  // remove field
  collection.fields.removeById("relation1806832074")

  return app.save(collection)
})
