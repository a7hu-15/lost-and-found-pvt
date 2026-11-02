import React from 'react';

interface LogoProps {
  className?: string;
  size?: 'sm' | 'md' | 'lg';
  showText?: boolean;
  titleText?: string;
  subtitleText?: string;
  variant?: 'dark' | 'light' | 'monochrome';
}

export const LogoIcon: React.FC<{ sizeClass?: string; className?: string }> = ({
  sizeClass = 'w-8 h-8',
  className = ''
}) => {
  return (
    <img
      src="/brand/refynd-logo.png"
      alt="ReFynd Logo"
      className={`${sizeClass} object-contain shrink-0 ${className}`}
    />
  );
};

export const Logo: React.FC<LogoProps> = ({
  className = '',
  size = 'md',
  showText = true,
  titleText = 'ReFynd',
  subtitleText = '',
  variant = 'dark'
}) => {
  const iconSizes = {
    sm: 'w-7 h-7',
    md: 'w-8 h-8',
    lg: 'w-10 h-10'
  };

  const textSizes = {
    sm: 'text-base',
    md: 'text-lg sm:text-xl',
    lg: 'text-xl sm:text-2xl'
  };

  const isLight = variant === 'light';
  const isMono = variant === 'monochrome';

  const isDefaultBrand = !subtitleText || titleText === 'ReFynd' || titleText === 'Cloud';

  return (
    <div className={`flex items-center gap-2.5 ${className}`}>
      {/* Master ReFynd Logo Icon */}
      <LogoIcon sizeClass={iconSizes[size]} />

      {/* Brand Text Lockup */}
      {showText && (
        <div className="flex items-center leading-none select-none">
          {isDefaultBrand ? (
            <>
              <span className={`font-extrabold tracking-tight ${textSizes[size]} ${isLight ? 'text-zinc-900' : 'text-white'}`}>
                Re
              </span>
              <span className={`font-extrabold tracking-tight ${textSizes[size]} ${isMono ? (isLight ? 'text-zinc-700' : 'text-zinc-300') : 'text-[#FF8A00]'}`}>
                Fynd
              </span>
            </>
          ) : (
            <div className="flex flex-col leading-none">
              <span className={`font-extrabold tracking-tight ${textSizes[size]} ${isLight ? 'text-zinc-900' : 'text-white'}`}>
                {titleText}
              </span>
              {subtitleText && (
                <span className={`font-semibold tracking-wide text-xs ${isMono ? (isLight ? 'text-zinc-700' : 'text-zinc-300') : 'text-[#FF8A00]'}`}>
                  {subtitleText}
                </span>
              )}
            </div>
          )}
        </div>
      )}
    </div>
  );
};

