// [start slot, length of slot], e.g. [6, 3]
type RawTimeslot = [number, number];

// list of timeslots, room
// e.g. [[[6, 3], [66, 3]], "34-101"
type RawSection = [Array<RawTimeslot>, string];

// following combiner_ws.py
type RawClass = {
  // no: "6.036", co: "6", cl: "036"
  no: string;
  co: string;
  cl: string;
  tb: boolean; // tba

  s: Array<string>; // subset of ["l", "r", "b"]
  l: Array<RawSection>; // lecture
  r: Array<RawSection>; // recitation
  b: Array<RawSection>; // lab
  // raw strings, e.g. T9.30-11 or TR1,F2
  lr: string;
  rr: string;
  br: string;

  // hass-h, hass-a, hass-s, hass-e
  hh: boolean;
  ha: boolean;
  hs: boolean;
  he: boolean;
  // ci-h, ci-hw
  ci: boolean;
  cw: boolean;
  // rest, lab, partial institute lab
  re: boolean;
  la: boolean;
  pl: boolean;

  // units of lecture, recitation, lab e.g. 5-0-7
  u1: number;
  u2: number;
  u3: number;

  // level: undergrad or grad
  le: "U" | "G";
  // comma-separated list of same classes
  // e.g. "21A.103, WGS.225"
  sa: string;
  // comma-separated list of meets with classes
  mw: string;

  // subset of ["FA", "JA", "SP", "SU"]
  t: Array<string>;
  // string describing prereqs
  // generally could be anything
  pr: string;
  
  d: string; // description
  n: string; // name
  i: string; // in-charge

  v: boolean; // virtual

  nx: boolean; // true if NOT offered next year
  rp: boolean; // can be repeated for credit
  u: string; // class url
  f: boolean; // has final

  ra: number; // rating from evals
  h: number; // hours from evals
  si: number; // size from evals
};