document.addEventListener('DOMContentLoaded', function () {
  var $deleteIcons = Array.prototype.slice.call(document.querySelectorAll('.delete'), 0);

  if ($deleteIcons.length > 0) {
    $deleteIcons.forEach(function($el) {
      console.log("adding event listener", $el);
      $el.addEventListener('click', function() {
        var target = $el.dataset.target,
          $target = document.getElementById(target);
        $target.remove();
      });
    });
  }
});
