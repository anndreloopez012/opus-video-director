import React from 'react';
import { interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';

export const MainComposition: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const scale = spring({
    frame: frame - 10,
    fps,
    config: {
      damping: 14,
      mass: 0.8,
      stiffness: 90,
    },
  });

  const opacity = interpolate(frame, [0, 15], [0, 1], {
    extrapolateRight: 'clamp',
  });

  return (
    <div
      style={{
        flex: 1,
        backgroundColor: '#0c0f1a',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        fontFamily: 'sans-serif',
      }}
    >
      <div
        style={{
          transform: `scale(${scale})`,
          opacity,
          textAlign: 'center',
        }}
      >
        <h1 style={{ color: '#e8b84b', fontSize: 72, margin: 0 }}>
          Opus 5.5 Remotion
        </h1>
        <p style={{ color: '#8b93b5', fontSize: 28, marginTop: 16 }}>
          Apple-Tier Kinetic Code Video
        </p>
      </div>
    </div>
  );
};
