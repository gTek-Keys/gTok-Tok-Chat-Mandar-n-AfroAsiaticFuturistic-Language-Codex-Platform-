const phases = [
  'Awakening', 'Embodiment', 'Instruction',
  'Voice', 'Understanding', 'Capabilities', 'Essence'
];

interface CodexPhaseTrackerProps {
  current: number;
}

export default function CodexPhaseTracker({ current }: CodexPhaseTrackerProps) {
  return (
    <div className="flex items-center justify-center my-6 space-x-4">
      {phases.map((phase, idx) => (
        <div key={phase} className={`text-xs text-center transition-all duration-300
          ${idx === current ? 'text-yellow-300 scale-110 font-bold' :
            idx < current ? 'text-green-400' : 'text-gray-500'}`}>
          <div className="w-4 h-4 mx-auto mb-1 rounded-full border
            border-current animate-pulse" />
          {phase}
        </div>
      ))}
    </div>
  );
}
