#!/usr/bin/node
exports.esrever = function (list) {
  const l = [];
  for (let i = list.length - 1; i >= 0; i--) {
    l.push(list[i]);
  }
  for (let i = 0; i < l.length; i++) {
    list[i] = l[i];
  }
  return list;
};
