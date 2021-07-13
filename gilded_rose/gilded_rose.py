class GildedRose(object):
    # These constants and a lot of the functions should live in Item, but I have stuck to the rules of the exercise
    MAX_QUALITY = 50
    MIN_QUALITY = 0
    BRIE_NAME = "Aged Brie"
    BACKSTAGE_PASSES_NAME = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS_NAME = "Sulfuras, Hand of Ragnaros"

    def __init__(self, items):
        self.items = items

    # I have left the "interface" of the class unchanged
    def update_quality(self):
        for item in self.items:
            if self._is_legendary(item):
                continue

            self._update_item_quality(item)
            item.sell_in -= 1
        
    def _update_item_quality(self, item):
        if item.name == GildedRose.BACKSTAGE_PASSES_NAME:
            self._update_backstage_passes_quality(item)
        elif item.name == GildedRose.BRIE_NAME:
            self._update_normal_item_quality(item, multiplier=-1)
        # new feature (test will need updating)
        # elif self._is_conjured_item(item):
        #     self._update_normal_item_quality(item, multiplier=2)
        else:
            self._update_normal_item_quality(item)

    def _update_backstage_passes_quality(self, passes):
        if passes.sell_in < 1:
            passes.quality = 0
        elif passes.sell_in < 6:
            self._change_quality_within_limits(passes, 3)
        elif passes.sell_in < 11:
            self._change_quality_within_limits(passes, 2)
        else:
            self._change_quality_within_limits(passes, 1)

    def _update_normal_item_quality(self, item, multiplier=1):
        normal_change = -1 if item.sell_in > 0 else -2
        self._change_quality_within_limits(item, normal_change * multiplier)

    def _change_quality_within_limits(self, item, change):
        new_quality = item.quality + change
        item.quality = max(GildedRose.MIN_QUALITY, min(GildedRose.MAX_QUALITY, new_quality))

    def _is_legendary(self, item):
        return item.name == GildedRose.SULFURAS_NAME

    def _is_conjured_item(self, item):
        return "conjured" in item.name.lower() # Actual business logic was not specified
