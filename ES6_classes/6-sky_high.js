import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this._floors = floors;
  }

  get sqft() {
    return this._sqft;
  }

  set floors(number) {
    if (typeof number !== 'number') {
      throw new TypeError('Floors must be a number');
    }
    this._floors = number;
  }

  get floors() {
    return this._floors;
  }

  evacuationWarningMessage() {
    return (`Evacuate slowly the ${this.floors} floors.`);
  }
}
