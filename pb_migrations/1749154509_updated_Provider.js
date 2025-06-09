/// <reference path="../pb_data/types.d.ts" />
migrate((app) => {
  const collection = app.findCollectionByNameOrId("pbc_737954259")

  // add field
  collection.fields.addAt(4, new Field({
    "hidden": false,
    "id": "number1158672400",
    "max": null,
    "min": null,
    "name": "telephone",
    "onlyInt": false,
    "presentable": false,
    "required": false,
    "system": false,
    "type": "number"
  }))

  return app.save(collection)
}, (app) => {
  const collection = app.findCollectionByNameOrId("pbc_737954259")

  // remove field
  collection.fields.removeById("number1158672400")

  return app.save(collection)
})
