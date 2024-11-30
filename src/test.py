from typing import List, Any

class Square():
    def __init__(self, length):
        self.

class AreaCalculator():
    def __init__(self, shapes: List[Any]):
        self._shapes = shapes
    
    def sum(self) -> float:
        for shape in self._shapes:
            if (isinstance(shape, ))
    {
        foreach ($this->shapes as $shape) {
            if (is_a($shape, 'Square')) {
                $area[] = pow($shape->length, 2);
            } elseif (is_a($shape, 'Circle')) {
                $area[] = pi() * pow($shape->radius, 2);
            }
        }

        return array_sum($area);
    }

    public function output()
    {
        return implode('', [
          '',
              'Sum of the areas of provided shapes: ',
              $this->sum(),
          '',
      ]);
    }
}